from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import DocumentForm
from .utils import process_document
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings 
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json




@csrf_exempt
def upload_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            process_document(document.file.path)
            return JsonResponse({'status': 'success', 'message': 'File uploaded and processed successfully.'})
        else:
            print(form.errors)
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Only POST method is allowed.'}, status=405)



# @csrf_exempt
# def upload_view(request):
#     # ▶️ Log at the very start
#     print("▶️ upload_view fired! Method:", request.method)
#     # Short-circuit and return immediately
#     return JsonResponse({'status':'hit!'}, status=200)

@csrf_exempt
def query_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            query = data.get('query')
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

        if not query or not query.strip():
            return JsonResponse({'status': 'error', 'message': 'Query cannot be empty'}, status=400)

        try:
            vectorstore = FAISS.load_local(
                "vectorstore",
                OpenAIEmbeddings(),
                allow_dangerous_deserialization=True
            )

            qa_chain = RetrievalQA.from_chain_type(
                llm=ChatOpenAI(model_name="gpt-4", temperature=0),
                chain_type="stuff",
                retriever=vectorstore.as_retriever(),
                return_source_documents=True,
            )

            response = qa_chain.invoke(query)

            return JsonResponse({
                'status': 'success',
                'answer': response.get('result'),
                'sources': [doc.page_content for doc in response.get('source_documents', [])]
            })

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Query error: {str(e)}'}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Only POST requests allowed'}, status=405)
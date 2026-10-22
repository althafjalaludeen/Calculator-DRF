from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads


@method_decorator(csrf_exempt, name='dispatch')
class AdditionView(View):
    def post(self,request):
        request_body = request.body         # Type of request body is JSON
        form_data = loads(request_body)     #Converting JSON to native Python Dictionary
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        result = n1 + n2
        print(request_body)
        data = {
            'message': 'Addition API is working fine',
            'SUM': result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class SubtractionView(View):
    def post(self,request):
        request_body = request.body         
        form_data = loads(request_body)     
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        result = n1 - n2
        print(request_body)
        data = {
            'message': 'Subtraction API is working fine',
            'DIFFERENCE': result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class MultiplicationView(View):
    def post(self,request):
        request_body = request.body        
        form_data = loads(request_body)     
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        result = n1 * n2
        print(request_body)
        data = {
            'message': 'Multiplication API is working fine',
            'PRODUCT': result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class DivisionView(View):
    def post(self,request):
        request_body = request.body        
        form_data = loads(request_body)     
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        result = n1 / n2
        print(request_body)
        data = {
            'message': 'Division API is working fine',
            'QUOTIENT': result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class ModulusView(View):
    def post(self,request):
        request_body = request.body         
        form_data = loads(request_body)     
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        result = n1 % n2
        print(request_body)
        data = {
            'message': 'Modulus API is working fine',
            'REMAINDER': result
        }
        return JsonResponse(data)

#BMI Calculator API

@method_decorator(csrf_exempt, name='dispatch')
class BMICalculatorView(View):
    def post(self,request):
        request_body = request.body         
        form_data = loads(request_body)     
        weight = form_data.get('weight')
        height = form_data.get('height')
        bmi = weight / (height ** 2)
        print(request_body)
        data = {
            'message': 'BMI Calculator API is working fine',
            'Height': height,
            'Weight': weight,
            'BMI': bmi
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class AgeView(View):
    def post(self,request):
        request_body = request.body         
        form_data = loads(request_body)     
        birth_year = form_data.get('birth_year')
        current_year = form_data.get('current_year')
        age = current_year - birth_year
        print(request_body)
        data = {
            'Age': age
        }
        return JsonResponse(data)

# For Persentage Calculation

@method_decorator(csrf_exempt,name='dispatch')
class PercentageView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        obtained_marks=form_data.get("obtained_marks")
        total_marks=form_data.get("total_marks")
        result=(obtained_marks/total_marks)*100
        data={
            "Percentage": result
        }
        return JsonResponse(data)

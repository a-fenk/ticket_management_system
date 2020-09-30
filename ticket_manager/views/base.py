from django.shortcuts import render, redirect

def base(request):
    if request.method == 'GET':

        if request.user.is_authenticated:
            return redirect('tickets')
        else:
            return render(
                request,
                'base.html',
            )
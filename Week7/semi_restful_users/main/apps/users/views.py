from django.shortcuts import render, redirect

def index(request):
    #creates a dictonary/key for users in database
    context = {
        "users:":User.objects.all()
    }
    return render(request, 'users/index.html', context)

def new(request):
    #Access the new html page
    return render(request, "users/new.html")

def create(request):
    #Validation of data POST
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field,message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('users/new')

    # Creates the user's account
    User.objects.create(
    first_name = request.POST['first_name'],
    last_name = request.POST['last_name'],
    email = request.POST['email']    
    )

    #redirect back to user index html
    return redirect('/users')

def edit(request,user_id):
    #Get User's ID
    context = {
        "user":User.objects.get(id=user_id)
    }

    #Send to Edit html using update method

    return render(request, 'users/{}/edit.html'.format(user_id), context)

def udpate(request,user_id):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field,message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/users/{}/edit'.format(user_id))

    Update_user = User.objects.get(id=user_id)
    Update_user.first_name = request.POST['first_name'],
    Update_user.last_name = request.POST['last_name'],
    Update_user.email = request.POST['email'] ,  
    Update.save() 
    
    
    return redirect('/users')

def show(request,user_id):

    context = {
        'user':User.objects.get(id=user_id)
    }
    return render(request, 'users/show.html', context)

def delete(request,user_id):

    User.objects.get(id=user_id).delete()

    return redirect('/users')
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Group
from .forms import UserForm, GroupForm


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})


def home_page(request):
    return render(request, 'base.html')


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()

    return render(request, 'add_user.html', {'form': form})


def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')

    else:
        form = UserForm(instance=user)

    return render(request, 'edit_user.html', {'form': form, 'user': user})


def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect('user_list')


def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            selected_users = request.POST.getlist('users')
            for user_id in selected_users:
                user = User.objects.get(pk=user_id)
                group.users.add(user)
            group.save()
            return redirect('group_list')
    else:
        form = GroupForm()

    return render(request, 'add_group.html', {'form': form})


def edit_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm(instance=group)

    return render(request, 'edit_group.html', {'form': form, 'group': group})


def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if group.can_be_deleted():
        group.delete()
        return redirect('group_list')
    else:
        return render(request, 'group_cannot_be_deleted.html', {'group': group})

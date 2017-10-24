import os

prefix_customer = 'uploads/user/'
prefix_menu = 'uploads/restaurant/'


def upload_user_profile(instance, filename):
    file_base, extension = filename.split(".")
    path_file = "{0:s}.{1:s}".format(str(instance.user.id), extension)
    return os.path.join(prefix_customer, path_file)


def upload_restaurant_menu(instance, filename):
    file_base, extension = filename.split(".")
    path_file = "{0:s}/{1:s}.{2:s}".format(str(instance.restaurant.id), str(file_base), extension)
    return os.path.join(prefix_menu, path_file)

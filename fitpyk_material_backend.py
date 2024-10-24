#


def background_generator(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p):
    background_p = []
    list_of_bckgrd_pts_x_p = []
    offset = 0.003
    decims = 3
    for count, pt in enumerate(list_of_bckgrd_pts_p):
        point = round(pt, decims)
        if count == 0:
            list_of_bckgrd_pts_x_p.append(str(point))
            list_of_bckgrd_pts_y_p[count] = str(list_of_bckgrd_pts_y_p[count])
            background_p.append(list_of_bckgrd_pts_x_p[count])
            background_p.append(list_of_bckgrd_pts_y_p[count])
        else:
            pt_left = round(point - offset, decims)
            pt_right = round(point + offset, decims)
            argmin_str_p = 'argmin(y if x > {} and x < {})'.format(pt_left, pt_right)
            min_str_p = 'min(y if x > {} and x < {})'.format(pt_left, pt_right)
            list_of_bckgrd_pts_x_p.append(argmin_str_p)
            list_of_bckgrd_pts_y_p.append(min_str_p)
            background_p.append(list_of_bckgrd_pts_x_p[count])
            background_p.append(list_of_bckgrd_pts_y_p[count])
    return background_p


def background_generator_V2(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p):
    background_p = []
    list_of_bckgrd_pts_x_p = []
    # offset = 0.005  # 0.003 before
    list_of_bckgrd_pts_p.sort()
    decims = 3
    for count, pt in enumerate(list_of_bckgrd_pts_p):
        point = round(pt, decims)
        if count == 0:
            list_of_bckgrd_pts_x_p.append(str(point))
            list_of_bckgrd_pts_y_p[count] = str(list_of_bckgrd_pts_y_p[count])
            background_p.append(list_of_bckgrd_pts_x_p[count])
            background_p.append(list_of_bckgrd_pts_y_p[count])
        else:
            pt_left = round(point - half_window_p, decims)
            pt_right = round(point + half_window_p, decims)
            x_str_p = '(argmin(y if x > {} and x < {}) + argmax(y if x > {} and x < {}))/2'.format(pt_left, pt_right, pt_left, pt_right)
            y_str_p = '(min(y if x > {} and x < {}) + max(y if x > {} and x < {}))/2'.format(pt_left, pt_right, pt_left, pt_right)
            list_of_bckgrd_pts_x_p.append(x_str_p)
            list_of_bckgrd_pts_y_p.append(y_str_p)
            background_p.append(list_of_bckgrd_pts_x_p[count])
            background_p.append(list_of_bckgrd_pts_y_p[count])
    return background_p


def region_divider(point, half_window_p, divs_p, decims):
    x_function_p = '('
    y_function_p = '('
    for i in range(divs_p):
        if i == 0:
            pt_left = round(point - half_window_p, decims)
            pt_right = round(point - half_window_p + (half_window_p/(divs_p/2)), decims)
        else:
            pt_left = round(pt_right, decims)
            pt_right = round(point - half_window_p + (i + 1)*(half_window_p/(divs_p/2)), decims)

        # MAY HAVE TO REPLACE THE <= with just <
        x_str_p = '(argmin(y if x > {} and x <= {}) + argmax(y if x > {} and x <= {}))/2'.format(pt_left, pt_right, pt_left,
                                                                                                 pt_right)
        y_str_p = '(min(y if x > {} and x <= {}) + max(y if x > {} and x <= {}))/2'.format(pt_left, pt_right, pt_left,
                                                                                           pt_right)

        # print(x_str_p)
        # print(y_str_p)

        if i != divs_p - 1:
            x_function_p = x_function_p + x_str_p + ' + '
            y_function_p = y_function_p + y_str_p + ' + '
        else:
            x_function_p = x_function_p + x_str_p + ')/{}'.format(divs_p)
            y_function_p = y_function_p + y_str_p + ')/{}'.format(divs_p)

        # print(i)
        # print(x_function_p)
        # print(y_function_p)
    return x_function_p, y_function_p


def background_generator_V3(list_of_bckgrd_pts_p, list_of_bckgrd_pts_y_p, half_window_p, divs_p):
    background_p = []
    list_of_bckgrd_pts_x_p = []
    # offset = 0.005  # 0.003 before
    list_of_bckgrd_pts_p.sort()
    decims = 3
    for count, pt in enumerate(list_of_bckgrd_pts_p):
        point = round(pt, decims)
        if count == 0:
            list_of_bckgrd_pts_x_p.append(str(point))
            list_of_bckgrd_pts_y_p[count] = str(list_of_bckgrd_pts_y_p[count])
            background_p.append(list_of_bckgrd_pts_x_p[count])
            background_p.append(list_of_bckgrd_pts_y_p[count])
        else:
            # pt_left = round(point - half_window_p, decims)
            # pt_right = round(point + half_window_p, decims)
            x_str_p, y_str_p = region_divider(point, half_window_p, divs_p, decims)
            # print(x_str_p)
            # print(y_str_p)
            list_of_bckgrd_pts_x_p.append(x_str_p)
            list_of_bckgrd_pts_y_p.append(y_str_p)
            background_p.append(list_of_bckgrd_pts_x_p[count])
            background_p.append(list_of_bckgrd_pts_y_p[count])

    # print(background_p)
    return background_p


def list_to_string(s):
    # initialize an empty string and a counter so that you don't add an extra space at the end
    str1 = ""
    counter = 0

    # traverse in the string
    for ele in s:
        counter += 1
        str1 += str(ele)
        if counter < len(s):  # add spaces between all strings and make sure to not add one after last entry
            str1 += ','

        # return string
    return str1


def bg_spline_generator(str_p):
    background_p = '%bg0 = Spline(' + str_p + ')'
    return background_p


if __name__ == "__main__":
    list_of_bckgrd_pts = [3.87, 5.147, 6.787, 8.547, 10.317, 11.597, 12.997, 13.997, 15.227, 15.997, 16.997, 17.847, 18.627, 18.947]
    # # list_of_bckgrd_pts_x = []  # argmin :: argmin(y if x > 15.225 and x < 15.229)
    list_of_bckgrd_pts_y = [0.168]  # min :: min(y if x > 15.225 and x < 15.229)
    #
    # # background_generator(list_of_bckgrd_pts, list_of_bckgrd_pts_y)
    # print(bg_spline_generator(list_to_string(background_generator(list_of_bckgrd_pts, list_of_bckgrd_pts_y))))
    # list_of_bckgrd_pts = [1, 5, 10]
    # list_of_bckgrd_pts_y = [1]
    # half_window = 0.025
    # divs = 4
    # print(bg_spline_generator(list_to_string(background_generator_V3(list_of_bckgrd_pts, list_of_bckgrd_pts_y, half_window, divs))))

    region_divider(5, 0.5, 10, 3)

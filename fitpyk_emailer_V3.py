import smtplib, ssl

# TEST EMAIL ACCOUNT
# ACCT: fitpyk.bot@gmail.com
# PWD:  Queensu2020!


def fitpyk_send_email(receiver_email_p, filename_prefix_p, first_file_p, number_of_spectra_p):
    port = 465  # for SSL
    smtp_server = 'smtp.gmail.com'
    sender_email = 'fitpyk.bot@gmail.com'
    password = 'Queensu2020!'

    if first_file_p == 1:
        message = """\
        Fitpyk Fitting Completed
        
        constrained fitting of {} spectra {} through {} completed.""".format(filename_prefix_p, first_file_p, number_of_spectra_p)
    else:
        message = """\
        Fitpyk Fitting Completed

        constrained fitting of {} spectra {} through {} completed.""".format(filename_prefix_p, first_file_p,
                                                                             number_of_spectra_p + first_file_p - 1)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email_p, message)


if __name__ == "__main__":
    receiver_email = 'lravkov@gmail.com'
    filename_prefix = 'K_Sample'
    first_file = 1
    number_spectra = 12
    fitpyk_send_email(receiver_email, filename_prefix, first_file, number_spectra)

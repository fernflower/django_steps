A blog-like django-based website (Python 3, Django 1.6.5)

## Installation

[Here](https://github.com/fernflower/ansible_django_steps) you can find ansible playbook to ease the pain of deployment. Clone the repo and follow the installation guide.

## Troubleshooting

### No VK comments on devserver
In order to enable VK comments on developer's server you need to start server at 127.0.0.1:80. 
The best way I found (to avoid starting server as root) - start server at port 8080 and redirect traffic to port 80
by adding entries to iptables.

```
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
sudo iptables -t nat -A OUTPUT -d localhost -p tcp --dport 80 -j REDIRECT --to-port 8080
```

### Setting up Gmail notifications 
In order to set up email notifications (gmail) on message post you need to create file 
contacts/secret_settings.py and setup Gmail's login\password and send mail list. Something like the following:

```
MY_EMAIL_HOST_USER = "my_login"
MY_EMAIL_HOST_PASSWORD = "my_pass"
MY_EMAIL_RECIPIENT_LIST = ("notify_me1@site.com", "notify_me2@site.com", )
```
All other settings (smtp port, smtp server etc are in mysite/settings.py as usual; these ones were moved out
and .gitignored for obvious security reasons)

Full list of custom secret settings you can see in mysite/secret_settings.sample

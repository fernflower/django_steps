<!DOCTYPE html>
<html lang="en">

<head>

    <link rel="shortcut icon" href="/{{static_url}}/freelancer/img/bass-clef.png" type="image/x-icon" />
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{% trans "Max Makagonov, professional multi-genre double bass/bass guitar player" %}" />
    <meta property="og:description" content="{% trans "Max Makagonov, professional multi-genre double bass/bass guitar player" %}" />
    <meta property="og:title" content="{% trans "Max Makagonov" %}" />
    <meta property="og:image" content="/{{static_url}}/freelancer/img/so_jazzy_small_square_300px.jpg" />
    <meta property="og:url" content="www.maxmakagonov.com" />
    <meta property="og:type" content="website" />
    <meta property="og:locale" content="en_GB" />
    <meta property="og:locale:alternate" content="ru_RU" />
    <meta name="keywords" content="{% trans "Max Makagonov,bass,double bass,bass guitar,jazz,funk,rock,pop,classical,music,Moscow,maxmakagonov.com,Maxim Makagonov,Maksim Makagonov,Magnitogorsk,musician,professional" %}" />
    <meta name="author" content="Inessa Vasilevskaya" />

    <title>{% trans "Max Makagonov - double bass player" %}</title>

    <!-- Bootstrap Core CSS -->
    <link href="/{{static_url}}/freelancer/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Theme CSS -->
    <link href="/{{static_url}}/freelancer/css/freelancer.min.css" rel="stylesheet">
    <!-- Flags css -->
    <link href="/{{static_url}}/flag-icon-css-master/css/flag-icon.min.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="/{{static_url}}/freelancer/vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body id="page-top" class="index">
<div id="skipnav"><a href="#maincontent">Skip to main content</a></div>
    <span itemscope itemtype="http://schema.org/Article">
    <!-- Navigation -->
    <nav id="mainNav" class="navbar navbar-default navbar-fixed-top navbar-custom">
        <meta itemprop="headline" content="{% trans "Max Makagonov - double bass player" %}">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header page-scroll">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span> {% trans "Menu" %}<i class="fa fa-bars"></i>
                </button>
                <a class="navbar-brand" href="#page-top"><span itemprop="name">{% trans "Max Makagonov" %}</span></a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav navbar-right">
                    <li class="hidden">
                        <a href="#page-top"></a>
                    </li>
                    <li class="page-scroll">
                        <a href="#portfolio">{% trans "Videos" %}</a>
                    </li>
                    <li class="page-scroll">
                        <a itemprop="url" href="#about">{% trans "About" %}</a>
                    </li>
                    <li class="page-scroll">
                        <a href="#contact">{% trans "Contact Me" %}</a>
                    </li>
                    <li>
                        <a href="/en"><span class="flag-icon-background flag-icon-gb" style="color:transparent">en</span></a>
                    </li>
                    <li>
                        <a href="/ru"><span class="flag-icon-background flag-icon-ru" style="color:transparent">ru</span></a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container-fluid -->
    </nav>

    <!-- Header -->
    <header>
        <div class="container" id="maincontent" tabindex="-1">
            <div class="row">
                <div class="col-lg-12" itemprop="image" itemscope itemtype="http://schema.org/ImageObject">
                    <link itemprop="url" href="http://www.maxmakagonov.com/{{static_url}}/freelancer/img/so_jazzy_small_square_300px.jpg">
                    <meta itemprop="thumbnail" content="http://www.maxmakagonov.com/{{static_url}}/freelancer/img/so_jazzy_small_square_300px.jpg">
                    <meta itemprop="height" content="300">
                    <meta itemprop="width" content="300">
                    <img class="img-responsive img-circle" src="/{{static_url}}/freelancer/img/so_jazzy_small_square_300px.jpg" alt="">
                    <div itemscope itemtype="http://schema.org/Person" class="intro-text">
                        <h1 itemprop="name" class="name">{% trans "Max Makagonov" %}</h1>
                        <hr class="star-light">
                        <span class="skills">{% trans "Double Bass" %} | {% trans "Bass Guitar" %}</span>
                        <meta itemprop="jobTitle" content="Musician">
                        <meta itemprop="alternateName" content="Maksim Makagonov">
                        <meta itemprop="name" content="Maxim Makagonov">
                        <meta itemprop="image" content="/{{static_url}}/freelancer/img/so_jazzy_small_square_300px.jpg">
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- Portfolio Grid Section -->
    <section id="portfolio">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 text-center">
                    <h2>{% trans "Videos" %}</h2>
                    <hr class="star-primary">
                </div>
            </div>
            <div class="row" id="videos_row">
                % for id, url, name, date, duration in videos: 
                <div class="col-sm-4 portfolio-item">
                    <a href="#" class="portfolio-link" data-toggle="modal">
                        <div class="caption">
                            <div class="caption-content">
                                <i class="fa fa-search-plus fa-3x"></i>
                            </div>
                        </div>
                        <div itemscope itemtype="http://schema.org/VideoObject" class="embed-responsive embed-responsive-4by3">
                            <link itemprop="url" href="{{ url }}">
                            <link itemprop="thumbnailUrl" href="https://img.youtube.com/vi/{{ id }}/0.jpg">
                            <meta itemprop="isFamilyFriendly" content="true">
                            <meta itemprop="uploadDate" content="{{ date }}">
                            <meta itemprop="name" content="{{ name }}">
                            <meta itemprop="description" content="{{ name }}">
                            <meta itemprop="thumbnail" content="https://img.youtube.com/vi/{{ id }}/0.jpg">
                            <meta itemprop="duration" content="{{ duration }}">
                            <iframe class="embed-responsive-item" allowfullscreen src="{{ url }}">
                            </iframe>
                        </div>
                    </a>
                </div>
                % end
            </div>
            <div class="row">
                <div class="col-xs-12 text-center">
                    <button id="show_more_videos_btn" onclick="insert_videos(videos_num,videos_block)" class="btn btn-success btn-lg" enabled="{{ more_videos }}">{% trans "More" %}</button>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="success" id="about">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 text-center">
                    <h2>{% trans "About" %}</h2>
                    <hr class="star-light">
                </div>
            </div>
            <div class="row">
                <div class="col-lg-4 col-lg-offset-2">
                    <meta itemprop="articleBody" content="{% trans "Born in December 06, 1990 in Magnitogorsk, Russia" %}.
                    {% trans "Started taking cello lessons at the age of eight" %}.
                    {% trans "In 2002 passed audition to Moscow Frederic Chopin College of Music Performing where took up the double bass" %}.
                    {% trans "During school years garnered top prizes in numerous musical competitions, including Young talents of Moscovia, Young composers Moscow, III international competition of young musicians, Forum Festival in St. Petersburg" %}.
                    {% trans "Was a student of Moscow State Tchaikovsky Conservatory throughout 2009 - 2012, graduated from Maimonides State Classical Academy in 2015.  At that time was a member of several orchestras, including chamber orchestra of Moscow Conservatory directed by F. P. Korobov, Entre Nous orchestra directed by A. Karimov (Grand Prix at Young Prague festival, Prague 2011), Moscow State University Theater of Ancient music orchestra directed by V. A. Kreisberg, Averkin's Big Bang, JazZyl Big Band" %}.
                    {% trans "Engaged in various musical projects, worked with Natalia Skvortsova, Dmitry Mospan, Alexander Zinger, Brill Brothers, Evgeny Pobozhy, Sergey Osokin, Grigory Seredin, Yaroslava Simonova, Ivan Dyma, Andrea Becarro and others" %}.
                    {% trans "Participated in numerous jazz festivals and competitions, including Gnesin Jazz, State college of Music pop & jazz art Guitar & Piano competions, AquaJazz, Igor Butman's Jazz seasons, Jazz May Penza, 1Jazz.ru Festival" %}.">
                    <p>{% trans "Born in December 06, 1990 in Magnitogorsk, Russia" %}.</p>
                    <p>
                    {% trans "Started taking cello lessons at the age of eight" %}.</p>
                    <p>{% trans "In 2002 passed audition to Moscow Frederic Chopin College of Music Performing where took up the double bass" %}.
                    {% trans "During school years garnered top prizes in numerous musical competitions, including Young talents of Moscovia, Young composers Moscow, III international competition of young musicians, Forum Festival in St. Petersburg" %}.
                    </p>
                    <p>
                    {% trans "Was a student of Moscow State Tchaikovsky Conservatory throughout 2009 - 2012, graduated from Maimonides State Classical Academy in 2015.  At that time was a member of several orchestras, including chamber orchestra of Moscow Conservatory directed by F. P. Korobov, Entre Nous orchestra directed by A. Karimov (Grand Prix at Young Prague festival, Prague 2011), Moscow State University Theater of Ancient music orchestra directed by V. A. Kreisberg, Averkin's Big Bang, JazZyl Big Band" %}.
                    </p>
                </div>
                <div class="col-lg-4">
                    <p>{% trans "Engaged in various musical projects, worked with Natalia Skvortsova, Dmitry Mospan, Alexander Zinger, Brill Brothers, Evgeny Pobozhy, Sergey Osokin, Grigory Seredin, Yaroslava Simonova, Ivan Dyma, Andrea Becarro and others" %}.
                    </p>
                    <p>
                    {% trans "Participated in numerous jazz festivals and competitions, including Gnesin Jazz, State college of Music pop & jazz art Guitar & Piano competions, AquaJazz, Igor Butman's Jazz seasons, Jazz May Penza, 1Jazz.ru Festival" %}.
                    </p>
                </div>
                <div class="col-lg-8 col-lg-offset-2 text-center">
                    <a href="/{{static_url}}/files/rider.pdf" class="btn btn-lg btn-outline">
                        <i class="fa fa-download"></i> {% trans "Technical Rider" %}
                    </a>
                </div>
            </div>
        </div>
    </section>
    <meta itemprop="author" content="fernflower">
    <meta itemprop="datePublished" content="2017-09-02T08:00:00+03:00">
    <span itemprop="publisher" itemscope itemtype="https://schema.org/Organization">
        <span itemprop="logo" itemscope itemtype="https://schema.org/ImageObject">
            <link itemprop="url" href="https://avatars0.githubusercontent.com/u/1619167?s=60">
            <meta itemprop="thumbnail" content="https://avatars0.githubusercontent.com/u/1619167?s=60" %}">
            <meta itemprop="width" content="60">
            <meta itemprop="height" content="60">
        </span>
        <meta itemprop="name" content="fernflower">
    </span>

    <!-- Contact Section -->
    <section id="contact">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 text-center">
                    <h2>{% trans "Contact Me" %}</h2>
                    <hr class="star-primary">
                </div>
            </div>
            <div class="row">
                <div class="col-lg-8 col-lg-offset-2">
                    <!-- To configure the contact form email address, go to mail/contact_me.php and update the email address in the PHP file on line 19. -->
                    <!-- The form should work on most web servers, but if the form is not working you may need to configure your web server differently. -->
                    <form name="sentMessage" id="contactForm" novalidate>
                        {% csrf_token %}
                        <div class="row control-group">
                            <div class="form-group col-xs-12 floating-label-form-group controls">
                                <label for="name">Name</label>
                                <input type="text" class="form-control" placeholder="{% trans "Name" %}" id="name" required data-validation-required-message="{% trans "Please enter your name." %}">
                                <p class="help-block text-danger"></p>
                            </div>
                        </div>
                        <div class="row control-group">
                            <div class="form-group col-xs-12 floating-label-form-group controls">
                                <label for="email">Email Address</label>
                                <input type="email" class="form-control" placeholder="{% trans "Email Address" %}" id="email" required data-validation-required-message="{% trans "Please enter your email address." %}">
                                <p class="help-block text-danger"></p>
                            </div>
                        </div>
                        <div class="row control-group">
                            <div class="form-group col-xs-12 floating-label-form-group controls">
                                <label for="phone">Phone Number</label>
                                <input type="tel" class="form-control" placeholder="{% trans "Phone Number" %}" id="phone" required data-validation-required-message="{% trans "Please enter your phone number." %}">
                                <p class="help-block text-danger"></p>
                            </div>
                        </div>
                        <div class="row control-group">
                            <div class="form-group col-xs-12 floating-label-form-group controls">
                                <label for="message">Message</label>
                                <textarea rows="5" class="form-control" placeholder="{% trans "Message" %}" id="message" required data-validation-required-message="{% trans "Please enter a message." %}"></textarea>
                                <p class="help-block text-danger"></p>
                            </div>
                        </div>
                        <br>
                        <div id="success"></div>
                        <div class="row">
                            <div class="form-group col-xs-12">
                                <button type="submit" class="btn btn-success btn-lg">{% trans "Send" %}</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="text-center">
        <div class="footer-above">
            <div class="container">
                <div class="row">
                    <div itemscope itemtype="http://schema.org/PostalAddress" class="footer-col col-md-4">
                        <h3>{% trans "Location" %}</h3>
                        <p>{% trans "Moscow, Russia" %}</p>
                        <meta itemprop="addressLocality" content="Moscow">
                        <meta itemprop="addressRegion" content="Russia">
                    </div>
                    <div class="footer-col col-md-4">
                        <h3>{% trans "Around the Web" %}</h3>
                        <ul class="list-inline">
                            <li>
                                <a href="https://www.instagram.com/maxmakagonov/" class="btn-social btn-outline"><span class="sr-only">Instagram</span><i class="fa fa-fw fa-instagram"></i></a>
                            </li>
                            <li>
                                <a href="https://vk.com/makayun" class="btn-social btn-outline"><span class="sr-only">VK</span><i class="fa fa-fw fa-vk"></i></a>
                            </li>
                            <li>
                                <a href="https://www.facebook.com/max.makagonov" class="btn-social btn-outline"><span class="sr-only">Facebook</span><i class="fa fa-fw fa-facebook"></i></a>
                            </li>
                            <li>
                                <a href="https://www.linkedin.com/in/max-makagonov-11851023/" class="btn-social btn-outline"><span class="sr-only">Linked In</span><i class="fa fa-fw fa-linkedin"></i></a>
                            </li>
                        </ul>
                    </div>
                    <div class="footer-col col-md-4">
                        <h3>{% trans "See also" %}</h3>
                        <p><a href="http://www.monkeyfolk.com/">Monkey Folk</a></p>
                        <p><a href="http://www.compromise-duo.com/index.php/en/">Compromise project</a></p>
                        <p><a href="http://www.m-artel.com/">М-Артель</a></p>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer-below">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12">
                        <a href="https://github.com/fernflower">fernflower</a> &copy; 2017
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <!-- Scroll to Top Button (Only visible on small and extra-small screen sizes) -->
    <div class="scroll-top page-scroll hidden-sm hidden-xs hidden-lg hidden-md">
        <a class="btn btn-primary" href="#page-top">
            <i class="fa fa-chevron-up"></i>
        </a>
    </div>

    <!-- jQuery -->
    <script src="/{{static_url}}/freelancer/vendor/jquery/jquery.min.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="/{{static_url}}/freelancer/vendor/bootstrap/js/bootstrap.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>

    <!-- Contact Form JavaScript -->
    <script src="/{{static_url}}/freelancer/js/jqBootstrapValidation.js"></script>
    <script src="/{{static_url}}/freelancer/js/contact_me.js"></script>
    <script src="/{{static_url}}/freelancer/js/insert_videos.js"></script>

    <!-- Theme JavaScript -->
    <script src="/{{static_url}}/"freelancer/js/freelancer.min.js"></script>

</span>
</body>

</html>

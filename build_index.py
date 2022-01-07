from airium import Airium
import json


def head(a, github=False):
    with a.head():
        a.meta(charset='utf-8')
        a.meta(content='width=device-width, initial-scale=1', name='viewport')
        a.meta(content='IE=edge', **{'http-equiv': 'X-UA-Compatible'})
        a.meta(content='Source Themes Academic 4.7.0', name='generator')
        a.meta(content='Kyunghyun Lee', name='author')
        a.meta(content='Ph.D Candidate', name='description')
        a.link(href='/', hreflang='en-us', rel='alternate')
        a.meta(content='#2962ff', name='theme-color')
        a.link(crossorigin='anonymous', href='https://cdnjs.cloudflare.com/ajax/libs/academicons/1.8.6/css/academicons.min.css', integrity='sha256-uFVgMKfistnJAfoCUQigIl+JfUaP47GrRKjf6CTPVmw=', rel='stylesheet')
        a.link(crossorigin='anonymous', href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.0-1/css/all.min.css', integrity='sha256-4w9DunooKSr3MFXHXWyFER38WmPdm361bQS/2KUWZbU=', rel='stylesheet')
        a.link(crossorigin='anonymous', href='https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.5.7/jquery.fancybox.min.css', integrity='sha256-Vzbj7sDDS/woiFS3uNKo8eIuni59rjyNGtXfstRzStA=', rel='stylesheet')
        a.link(crossorigin='anonymous', href='https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.5.1/leaflet.css', integrity='sha256-SHMGCYmST46SoyGgo4YR/9AlK1vf3ff84Aq9yK4hdqM=', rel='stylesheet')
        a.script(async_='', crossorigin='anonymous', integrity='sha256-Md1qLToewPeKjfAHU1zyPwOutccPAm5tahnaw7Osw0A=', src='https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.1.2/lazysizes.min.js')
        a.link(href='https://fonts.googleapis.com/css?family=Montserrat:400,700%7CRoboto:400,400italic,700%7CRoboto+Mono&display=swap', rel='stylesheet')
        a.link(href='static/css/academic.css', rel='stylesheet')
        a.link(href='static/index.xml', rel='alternate', title='Kyunghyun Lee', type='application/rss+xml')
        a.link(href='static/index.webmanifest', rel='manifest')
        a('<!-- <link rel="icon" type="image/png" href="/images/icon_hu2065e2b3e3f9ec61858579cdb7515c4d_74858_32x32_fill_lanczos_center_2.png">\n  <link rel="apple-touch-icon" type="image/png" href="/images/icon_hu2065e2b3e3f9ec61858579cdb7515c4d_74858_192x192_fill_lanczos_center_2.png"> -->')
        a.link(href='/', rel='canonical')
        a.meta(content='summary', property='twitter:card')
        a.meta(content='Kyunghyun Lee', property='og:site_name')
        a.meta(content='/', property='og:url')
        a.meta(content='Kyunghyun Lee', property='og:title')
        # a.meta(content='Assistant Professor', property='og:description')
        a.meta(content='img/map[gravatar:%!s(bool=false) shape:circle]', property='og:image')
        a.meta(content='img/map[gravatar:%!s(bool=false) shape:circle]', property='twitter:image')
        a.meta(content='en-us', property='og:locale')
        with a.script(type='application/ld+json'):
            a('{\n  "@context": "https://schema.org",\n  "@type": "WebSite",\n  "potentialAction": {\n    "@type": "SearchAction",\n    "target": "/?q={search_term_string}",\n    "query-input": "required name=search_term_string"\n  },\n  "url": "/"\n}')

        a.title(_t='Kyunghyun Lee')


def body_headbar(a, github=False):
    with a.nav(klass='navbar navbar-expand-lg navbar-light compensate-for-scrollbar', id='navbar-main'):
        with a.div(klass='container'):
            with a.div(klass='d-none d-lg-inline-flex'):
                a.a(klass='navbar-brand', href='/', _t='Kyunghyun Lee')
            with a.button(klass='navbar-toggler', type='button', **{'aria-controls': 'navbar',
                                                                    'aria-expanded': 'false',
                                                                    'aria-label': 'Toggle navigation',
                                                                    'data-target': '#navbar-content',
                                                                    'data-toggle': 'collapse'}):
                with a.span():
                    a.i(klass='fas fa-bars')
            with a.div(klass='navbar-brand-mobile-wrapper d-inline-flex d-lg-none'):
                a.a(klass='navbar-brand', href='/', _t='Kyunghyun Lee')
            with a.div(klass='navbar-collapse main-menu-item collapse justify-content-start', id='navbar-content'):
                with a.ul(klass='navbar-nav d-md-inline-flex'):
                    with a.li(klass='nav-item'):
                        with a.a(klass='nav-link', href='/#about', **{'data-target': '#about'}):
                            a.span(_t='Home')
                    with a.li(klass='nav-item'):
                        with a.a(klass='nav-link', href='/#papers', **{'data-target': '#papers'}):
                            a.span(_t='Publications')
                    # with a.li(klass='nav-item'):
                    #     with a.a(klass='nav-link', href='/#awards', **{'data-target': '#awards'}):
                    #         a.span(_t='Awards & Honors')
                    # with a.li(klass='nav-item'):
                    #     with a.a(klass='nav-link', href='/#activities', **{'data-target': '#activities'}):
                    #         a.span(_t='Activities')


def body_profile(a, github=False):
    with a.div(id='profile'):
        a.img(alt='Avatar', klass='avatar avatar-circle', src='static/authors/admin/profile.jpg')
        with a.div(klass='portrait-title'):
            a.h2(_t='Kyunghyun Lee')
            a.h3(_t='Ph.D Candidate')
            with a.h3():
                with a.a(href='https://ee.kaist.ac.kr/', rel='noopener', target='_blank'):
                    a.span(_t='Robotics Program, Electrical Engineering, KAIST')
        with a.td():
            a.br()
            with a.a(href='cv/CVCVCVCVCVCVCVCVCV.pdf'):
                a.b(_t='CV')
            a('|')
            with a.a(href='https://scholar.google.com/citations?user=WOBfTQoAAAAJ&hl=ko'):
                a.b(_t='Google Scholar')
            a('|')
            with a.a(href='https://github.com/KyunghyunLee'):
                a.b(_t='Github')
            a.br()
            a.br()


def body_research_interest(a, github=False):
    a.br()
    with a.p():
        a('I am a Ph.D. student advised by Professor')
        a.a(href='http://rcv.kaist.ac.kr', _t='In So Kweon,')
        a('at')
        a.a(href='https://ee.kaist.ac.kr/', rel='noopener', target='_blank', _t='Electrical Engineering,')
        a.a(href='https://kaist.ac.kr/', rel='noopener', target='_blank', _t='KAIST.')

    with a.p():
        a('My research interests lie in Machine Learning, Reinforcement Learning and Robotics.')

    with a.p():
        a('My research topics include\n')

        with a.ul():
            a.li(_t='Reinforcement Learning')
            a.li(_t='Evolutionary Algorithms')
            a.li(_t='Reinforcement Learning Combined with Computer Vision')
            a.li(_t='Multi-agent Reinforcement Learning in Real-world Robotics System')


def body_contact(a, github=False):
    a.h3(_t='Contact')
    with a.ul(klass='ul-contact fa-ul'):
        with a.li():
            a.i(klass='fa-li fas fa-envelope')
            with a.div(klass='description'):
                a.p(klass='course', _t='kyunghyun.lee [at] kaist.ac.kr')

        with a.li():
            a.i(klass='fa-li fas fa-map-marker')
            with a.div(klass='description'):
                a.p(klass='course', _t='Bldg N1, Rm 211, 291 Daehak-ro, Yuseong-gu, Daejeon, Korea, 34141')


def body_education(a, github=False):
    a.h3(_t='Eduction')
    with a.ul(klass='ul-edu fa-ul'):
        with a.li():
            a.i(klass='fa-li fas fa-graduation-cap')
            with a.div(klass='description'):
                a.p(klass='course', _t='MS in Aerospace Engineering, 2015')
                a.p(klass='institution', _t='Seoul National University (SNU), Korea')
                a.p(klass='explanation',
                    _t='Thesis: "Development of A* Real-time Path Planning Algorithm of UAV Considering Collision Avoidance')
                a.p(klass='explanation', _t='Advisor: Youdan Kim')

        with a.li():
            a.i(klass='fa-li fas fa-graduation-cap')
            with a.div(klass='description'):
                a.p(klass='course', _t='BS in Mechanical Engineering, 2012')
                a.p(klass='institution', _t='Pohang University of Science and Technology (Postech), Korea')
                a.p(klass='explanation', _t='GPA: 3.81/4.3')


def body_experiences(a, github=False):
    with a.div(klass='container'):
        with a.div(klass='row'):
            with a.div(klass='col-lg-12'):
                a.h1(_t='Experiences')

                with a.ul():
                    with a.li():
                        with a.div(style='float:left'):
                            a.b(_t='The Robotics Institute, Carnegie Mellon University,')
                            a('Pittsburgh PA, USA')
                        a.div(style='float:right', _t='Jun 2019 - Aug 2019')
                        a.br()
                        a('Visiting Researcher')
                        a.br()
                        a('Advisor: Jean Oh, Martial Hebert')

                    with a.li():
                        with a.div(style='float:left'):
                            with a.b():
                                a.a(href='https://www.uvify.com/', _t='UVify, Inc.,', rel="noopener noreferrer nofollow")
                            a('Seoul, Korea')
                        a.div(style='float:right', _t='Mar 2015 - Jul 2018')
                        a.br()
                        a('CPO')
                        a.br()
                        a('Electoronics and software engineering in ')
                        a.a(href='https://www.uvify.com/oori/', _t='OORI', rel="noopener noreferrer nofollow")
                        a(' and ')
                        a.a(href='https://www.uvify.com/draco/', _t='DRACO', rel="noopener noreferrer nofollow")


def build_paper_tag_from_json(a, paper_json, github=False):

    if 'thumbnail' in paper_json and paper_json['thumbnail'] is not None:
        if isinstance(paper_json['thumbnail'], list):
            count = len(paper_json['thumbnail'])
            percent = int(100/count)
            for src in paper_json['thumbnail']:
                with a.div(klass='imghalf'):
                    a.img(alt='', klass='img-responsive', src=src)
        else:
            with a.div(klass='img'):
                src = paper_json['thumbnail']
                a.img(alt='', klass='img-responsive', src=src)

    else:
        with a.div(klass='img'):
            src = 'static/papers/images/blank.png'
            a.img(alt='', klass='img-responsive', src=src)

    with a.div(klass='description'):
        a.p(klass='title', _t=paper_json['title'])
        with a.p(klass='authors'):
            equal = False
            author_count = len(paper_json['authors'])
            count = 0
            for author in paper_json['authors']:
                count += 1
                if count != author_count:
                    comma = ','
                else:
                    comma = ''

                if 'Kyunghyun Lee' in author:
                    a.b(_t=author + comma)
                else:
                    a(author + comma)

                if '*' in author:
                    equal = True
            if equal:
                a(' (* Equal contribution)')

        with a.p(klass='venue'):
            if 'venue' in paper_json and paper_json['venue'] is not None:
                venue = paper_json['venue']
                if not isinstance(venue['publisher'], list):
                    publishers = [venue['publisher']]
                else:
                    publishers = venue['publisher']
                for publisher1 in publishers:
                    a(publisher1)

                if 'publisher_acr' in venue:
                    a.b(f'({venue["publisher_acr"]}), ')

                if 'special' in venue and venue['special'] is not None:
                    a(str(venue['year']) + ', ')
                    special = venue['special']
                    a.span(style='font-weight:bolder;color:#BB2222', _t=special['type'])
                    if 'comment' in special and special['comment'] is not None:
                        a.span(style='font-weight:normal', _t='(' + special['comment'] + ')')
                else:
                    a(venue['year'])
            else:
                a('Under Review')

            a.span(style='font-weight:normal')

        with a.p(klass='resources'):
            resources = paper_json['resources']
            resource_counter = len(resources.keys())
            count = 0
            if resource_counter == 0:
                a('[ paper ]')
            else:
                a('[')
                # sorted_key = sorted(resources.keys())
                for key in resources.keys():
                    # key_text = key.split('_')[1:]
                    # key_text = '_'.join(key_text)
                    a.a(href=resources[key], _t=key)
                    count += 1
                    if count != resource_counter:
                        a(' / ')
                a(']')

        # a.p(klass='resources', _t='[ paper ]')


def body_publications(a, github=False):
    with open('papers.json', 'rt', encoding='UTF8') as f:
        paper_info = json.load(f)

    paper_key_sorted = sorted(paper_info.keys())
    paper_key_reversed = reversed(paper_key_sorted)
    with a.div(klass='container'):
        with a.div(klass='row'):
            with a.div(klass='col-lg-12'):
                a.h1(_t='Publications')
            with a.div(klass='row'):
                with a.ul(klass='ul-papers'):
                    for paper_key in paper_key_reversed:
                        with a.li():
                            paper = paper_info[paper_key]
                            build_paper_tag_from_json(a, paper)


def body_academic(a, github=False):
    with a.div(klass='container'):
        with a.div(klass='row'):
            with a.div(klass='col-lg-12'):
                a.h1(_t='Academic Activities')
                a.h2(id='reviewer', _t='Reviewer')
                with a.ul():
                    a.li(_t='NeurIPS 2021')
                    a.li(_t='ICLR 2022')
                    a.li(_t='ICML 2022')


def body(a, github=False):
    with a.body(id='top', **{'data-offset': '70', 'data-spy': 'scroll', 'data-target': '#navbar-main'}):
        body_headbar(a, github)

        a.span(klass='js-widget-page d-none')
        with a.section(klass='home-section wg-about', id='about', style='padding: 30px 0 20px 0;'):
            with a.div(klass='container'):
                with a.div(klass='row'):
                    with a.div(klass='col-12 col-lg-4'):
                        body_profile(a, github)
                    with a.div(klass='col-12 col-lg-8'):
                        body_research_interest(a, github)

                        with a.div(klass='row'):
                            with a.div(klass='col-md-6'):
                                body_contact(a, github)
                            with a.div(klass='col-md-6'):
                                body_education(a, github)

        with a.section(klass='home-section wg-blank', id='experience', style='padding: 10px 0 10px 0;'):
            body_experiences(a, github)

        with a.section(klass='home-section wg-papers', id='papers', style='padding: 20px 0 20px 0;'):
            body_publications(a, github)

        with a.section(klass='home-section wg-papers', id='papers', style='padding: 20px 0 20px 0;'):
            body_academic(a, github)

        with a.a(href='https://hits.seeyoufarm.com'):
            a.img(src='https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fkyunghyunlee.github.io&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false')


def main():
    flask_html = Airium()
    github_html = Airium()

    a = flask_html
    b = github_html

    a('<!DOCTYPE html>')
    b('<!DOCTYPE html>')

    with a.html(lang='en'):
        head(a)
        body(a)

    with b.html(lang='en'):
        head(b, github=True)
        body(b, github=True)

    with open('templates/_index.html', 'wt', encoding='UTF-8') as f:
        f.write(str(flask_html))

    with open('index.html', 'wt', encoding='UTF-8') as f:
        f.write(str(github_html))


if __name__ == '__main__':
    main()

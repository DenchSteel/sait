from flask import Flask, request, make_response, session, render_template, redirect, abort, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from data.news import News
from data.users import User, LoginForm
from forms.news import NewsForm
from forms.user import RegisterForm
from data import db_session, news_api
from data.val import Currency


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found yet'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/index")
def news():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


@app.route("/stock")
def stock():
    pass


@app.route("/currency")
def currency():
    USD_ = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
    EUR_ = "https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=APwXEdde0l1Zlvua1JTMXxovQDoOrb3yyQ%3A1683356678622&ei=BvxVZKXQJYf1rgTuvI_wBg&oq=%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMg0IABCKBRCxAxCDARBDMg0IABCKBRCxAxCDARBDMg0IABCKBRCxAxCDARBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDMgcIABCKBRBDOgoIABBHENYEELADOgoIABCKBRCwAxBDOgUIABCABDoKCAAQgAQQFBCHAjoHCAAQgAQQCjoGCAAQFhAeOgkIABCABBAKECo6CAgAEBYQHhAKOgcIIxCKBRAnOgsIABCABBCxAxCDAToICAAQgAQQsQM6DAgjEIoFECcQRhCCAjoQCAAQgAQQFBCHAhCxAxCDAToOCAAQgAQQsQMQgwEQyQM6CAgAEIAEEJIDOgsIABCKBRCxAxCDAToRCC4QgAQQsQMQgwEQxwEQ0QM6CwguEIoFELEDEIMBOgcIIxDqAhAnOg8IABCKBRDqAhC0AhBDGAE6CwguEIMBELEDEIoFSgQIQRgAUN8FWOdPYLdaaANwAXgBgAH2A4gBlhiSAQwwLjExLjIuMS4wLjGYAQCgAQGwARTIAQrAAQHaAQYIARABGAE&sclient=gws-wiz-serp"
    CNY_ = "https://www.google.com/search?q=%D1%8E%D0%B0%D0%BD%D1%8C+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=APwXEdeXRCPWu48hol3cebaiTBtgJMqWKA%3A1683356745180&ei=SfxVZNXRCoKSwPAPtpiooAo&oq=%D1%8E+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB5KBAhBGABQAFjWHWDlMGgBcAF4AIABswOIAZgHkgEHMC4zLjQtMZgBAKABAcABAQ&sclient=gws-wiz-serp"
    GBP_ = "https://www.google.com/search?q=%D1%84%D1%83%D0%BD%D1%82+%D1%81%D1%82%D0%B5%D1%80%D0%BB%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=APwXEdcKsJg6HSBV_oUN6QoPqRV0KvwQVw%3A1683358015833&ei=PwFWZPLDMo-yqwHropH4CQ&oq=%D1%84%D1%83%D0%BD%D1%82+%D1%81+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB46CggAEA0QgAQQsQM6BwgAEA0QgAQ6CggAEIoFELEDEEM6BwgAEIoFEEM6BQgAEIAEOg8IABCKBRCxAxBDEEYQggJKBAhBGABQAFiPGmDHKWgAcAF4AIABhAOIAdwIkgEHMC41LjAuMZgBAKABAcABAQ&sclient=gws-wiz-serp"
    CHF_ = "https://www.google.com/search?q=%D1%88%D0%B2%D0%B5%D0%B9%D1%86%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9+%D1%84%D1%80%D0%B0%D0%BD%D0%BA+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=APwXEdfiPLT_-vQy5lam1PDvIFiTFtKGzQ%3A1683358517974&ei=NQNWZOaOO-bIrgS_-LvYDg&oq=%D1%89+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgBMgsIABAHEB4Q8QQQCjILCAAQBxAeEPEEEAoyCAgAEAgQBxAeMgoIABAFEAcQHhAKOgoIABBHENYEELADOgoIABCKBRCwAxBDSgQIQRgAULsOWLsOYPEfaAFwAXgAgAGXAYgBlwGSAQMwLjGYAQCgAQHIAQrAAQE&sclient=gws-wiz-serp"

    USD = Currency(USD_).check_currency("Доллар")
    EUR = Currency(EUR_).check_currency("Евро")
    CNY = Currency(CNY_).check_currency("Юань")
    GBP = Currency(GBP_).check_currency("Фунт стерлинга")
    CHF = Currency(CHF_).check_currency("Швейцарский франк")

    return render_template("o_sait.html", title="Курс валют", usd=USD, eur=EUR, cny=CNY, gbr=GBP, chf=CHF)


@app.route("/")
def sait():
    return render_template("o_sait.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/news', methods=['GET', 'POST'])
@login_required
def add_news():
    form = NewsForm()
    if request.method == "GET":
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            news = News()
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            current_user.news.append(news)
            db_sess.merge(current_user)
            db_sess.commit()
            return redirect('/')
        return render_template('news.html', title='Добавление новости',
                               form=form)
    if request.method == "POST":
        return


@app.route('/news/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = NewsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user
                                          ).first()
        if news:
            form.title.data = news.title
            form.content.data = news.content
            form.is_private.data = news.is_private
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id, News.user == current_user).first()
        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            db_sess.commit()
            return redirect('/index')
        else:
            abort(404)
    return render_template('news.html',
                           title='Редактирование новости',
                           form=form
                           )


@app.route('/news_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id,
                                      News.user == current_user
                                      ).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route("/cookie_test")
def cookie_test():
    visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(
            f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response(
            "Вы пришли на эту страницу в первый раз за последние 2 года")
        res.set_cookie("visits_count", '1',
                       max_age=60 * 60 * 24 * 365 * 2)
    return res


@app.route("/session_test")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(news_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()
    # app.run(port=5000, host='127.0.0.1')

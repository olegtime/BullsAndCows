from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from forms import StartForm, PlayForm
from game import Game

app = Flask(__name__)
app.config.from_object(Config)

game = Game()


@app.route('/', methods=['get', 'post'])
def index():
    form = StartForm()
    if form.validate_on_submit():
        if not form.size.data.isdigit() or int(form.size.data) > 9 or int(form.size.data) < 3:
            flash(f'Неверная длина числа. Попробуйте еще раз.',
                  'error')
            return redirect(url_for('index'))
        game.start(form.size.data)
        return redirect(url_for('play'))
    return render_template('index.html', form=form)


@app.route('/rules', methods=['get', 'post'])
def rules():
    return render_template('rules.html')


@app.route('/play', methods=['get', 'post'])
def play():
    form = PlayForm()
    if form.validate_on_submit():
        attempt = form.attempt.data
        if not str(attempt).isdigit():
            flash(f'Было введено не число. Попробуйте еще раз.', 'error')
            return redirect(url_for('play'))
        if len(attempt) != game.number_size:
            flash(f'Число неверной длины (длина загаданного числа - {game.number_size}). Попробуйте еще раз.', 'error')
            return redirect(url_for('play'))

        bulls_and_cows = game.guess(attempt)

        if bulls_and_cows == [game.number_size, 0]:
            return render_template('play.html', attempts=game.attempts, win=True)

        return render_template(
            'play.html',
            form=form,
            error=False,
            attempts=game.attempts
        )

    return render_template(
        'play.html',
        form=form,
        error=False,
        attempts=game.attempts
    )


if __name__ == '__main__':
    app.run()




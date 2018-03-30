# Flask Template

## Development

```shell
pip install virtualenv # global
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
export PORT=5000 # optional
export FLASK_DEBUG=1 # optional
python main.py
```

## Packages

- Python 3.6
- Flask
- requests
- beautifulsoup4
- gunicorn

## Notes

```shell
# Deploy using Heroku Git
git remote add heroku https://git.heroku.com/???.git # or heroku git:remote -a ???
git push heroku master

# Copy to new project
cp -r flask-template/ new-project/
cd new-project/
rm -rf .git
vim README.md
git init
```


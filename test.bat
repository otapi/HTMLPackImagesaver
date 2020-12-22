rem create new folder and copy the built package from the dist folder first!
virtualenv -p python3 .
scripts\activate.bat

rem #install
rem pip install -r requirements.txt

rem update the version number accordingly

pip install HTMLPackImagesaver-0.0.2.tar.gz
python -m HTMLPackImagesaver


pip install HTMLPackImagesaver
python -m HTMLPackImagesaver
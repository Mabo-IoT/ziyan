title reinstall-ziyan
pip uninstall -y ziyan 1>nul
cd ../..
if exist build rd /s /q build
echo 'clean build/'
python setup.py install 1>nul
echo 'good'
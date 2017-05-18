#!/bin/sh

# 쉽게 간편하게 테스트를 실행 
# cd ../myproject && python manage.py test --settings=myproject.settings.development

 cd ../myproject && pytest -s 

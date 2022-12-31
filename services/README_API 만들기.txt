1. 횡전개 (완료):
    Incident,Problem,Change,Request,Capacity,Backup,Instance,Kubernetes
    Database,License,Vulnerability,Preventive(PM),Discussion(Topic)

2. Approach
  Step1. models.py
      -> field 확인
  Step2. curds/xxxx.py
      -> field 갱신(확인)
      -> update() 내 .first() 추가, 인수 type Schema 삭제
  Step3. schema.py
      -> field 갱신(확인)
  Step4. routers/xxxx.py
      -> field 갱신(확인)
      -> schema 참조 갱신
  Step5. Test with httpie
  Step6. xxxxList.vue
      -> field 갱신(확인)
      -> API_URL 및 field 수정
  Step7. xxxxDetail.vue 갱신
      -> field 갱신(확인)
      -> close() 내 setDefaultItem() 삭제
  Step8. CRUD Test
      -> 화면 test
from django.test import TestCase
# Create your tests here.
from rest_framework.test import APIRequestFactory
from .views import NoteListCreate
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from django.urls import reverse,resolve,include,path
from rest_framework import status
from rest_framework.test import APITestCase,RequestsClient,URLPatternsTestCase
from django.contrib.auth.models import User
from .models import Note
import json
from django.test.client import encode_multipart, RequestFactory
from .views import NoteListRetrive,NoteListCreate
from django.contrib.auth.models import User
from django.test import SimpleTestCase,Client
from requests.auth import HTTPBasicAuth







#basc


# #***********class base django test cases url*****************
#class NoteTests(SimpleTestCase):
#     def test_url_classbase(self):
#         url = reverse('note-list-create')
#         resolved_view = resolve(url).func
#         self.assertEqual(resolved_view.view_class,NoteListCreate)

#********method 2****************
    #  def test_url_funcbase(self):
    #      url =reverse('note-list-create')
    #      self.assertEqual(resolve(url).func.view_class, NoteListCreate)


# #**************function base django tests url***************
#     def test_url_funcbase(self):
#         url =resolve('note-list-create')
#         self.assertDictEquals(resolve(url).func,NoteListCreate)
    
#******************Pk url TEST CASES*****************************
    # def test_url_pk(self):
    #     #for another arguments in url field
    #      #url = reverse('note-list-retrieve', kwargs={'slug': 'example-slug', 'pk': 1, 'name': 'example-name'})
    #     url = reverse('note-list-retrive',kwargs={'pk':1})
    #     self.assertEqual(resolve(url).func.view_class,NoteListRetrive)
 
#**********************End Url Test cases **********************
    
#*********************************************************************
    #*******************Started View Test Cases**********************#
#*********************************************************************
# class NoteTests(TestCase):
    # def test_creteview(self):
    #     client =Client()
    #     response = client.get(reverse('note-list-create'))
    #     self.assertEqual(response.status_code,status.HTTP_200_OK)
    #     #self.assertTemplateUsed(response,'api/create.html')


























#************************Rest Api TEST CASES ********************

#***********************************Final Api work view based********************************

    
    # def test_create_note(self):
    #     data = {
    #         'title':'Junglebook',
    #         'content':'Jungle Jungle Baat Chali hai'
    #     }
    #     _response = self.client.post(reverse('note-list-create'),data=data,format='json')
    #     create_data = _response.json()
    #     self.assertEqual(_response.status_code,status.HTTP_201_CREATED)
    #     print(create_data)

#     def test_get_note(self):
#         data = {
#             'title':'Junglebook',
#             'content':'Jungle Jungle Baat Chali hai'
#         }
#         _response=self.client.get(reverse('note-list-create'),data=data,format='json')
#         get_data = _response.json()
#         self.assertEqual(_response.status_code,status.HTTP_200_OK)
#         print(get_data)

#     def test_put_note(self):
#         create_data = {
#             'title':'Mybio',
#             'content':'Mai Asa kyu Hoon'
#         }
#         _response = self.client.post(reverse('note-list-create'),data=create_data,format='json')
#         self.assertEqual(_response.status_code,status.HTTP_201_CREATED)
#         _response_data = _response.json()['id']
#         print(_response_data)

#         url = reverse('note-list-retrive',kwargs={'pk':_response_data})

#         update_data = {
#             'title':'Tarzer',
#             'content':'Tarzen The wonder car'
#         }

#         response =self.client.put(url,data=update_data,format='json')
#         self.assertEqual(response.status_code,status.HTTP_200_OK)
#         latest_data = response.json()
#         print(latest_data)

#         get_response = self.client.get(url,format='json')
#         get_book_data = get_response.json()
#         print(get_book_data)
    
    

#     def test_patch_note(self):
#         # Step 1: Create a new note
#         create_data = {
#             'title': 'Mybio',
#             'content': 'Mai Asa kyu Hoon'
#         }
#         create_response = self.client.post(reverse('note-list-create'), data=create_data, format='json')
#         self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        
#         # Extract the created note's ID
#         created_id = create_response.json()['id']
#         print(created_id)

#         # Step 2: Update the created note
#         url = reverse('note-list-retrive', kwargs={'pk': created_id})
#         update_data = {
#             'title': 'Tarzen'
#         }
#         update_response = self.client.patch(url, data=update_data, format='json')
#         self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        
#         # Verify the updated data
#         updated_data = update_response.json()
#         print(updated_data)

#         # Step 3: Retrieve the updated note to verify the patch
#         get_response = self.client.get(url, format='json')
#         final_data = get_response.json()
#         print(final_data)

#         # Additional assertions can be made here
#         self.assertEqual(final_data['title'], 'Tarzen')
        

#     def test_note_delete(self):
#         data = {
#             'title':'Junglebook',
#             'content':'Jungle Jungle Baat Chali hai'
#         }
#         _response = self.client.post(reverse('note-list-create'),data=data,format='json')
#         self.assertEqual(_response.status_code,status.HTTP_201_CREATED)
#         create_data = _response.json()['id']
#         print(create_data)

#         url = reverse('note-list-retrive',kwargs={'pk':create_data})

#         _response = self.client.delete(url)
#         print(_response.content)
#         self.assertEqual(_response.status_code,status.HTTP_204_NO_CONTENT)
        
#         get_deleed_data = self.client.get(url,format='json')
#         get_data = get_deleed_data.json()

#         print(get_data)


 



    

#********************************Django Rest api website **************************


class NoteTests(APITestCase):

#     def test_fac(self):
#         factory = APIRequestFactory()
#         request = factory.post('/notes/', json.dumps({'title': 'new idea'}), content_type='application/json'   
    
    
#     def test_put(self):
#         factory = APIRequestFactory()
#         request = factory.put('/notes/',{'title':'Mogli','content':'Jungle Jungle Baat Chali hai'})
#         request = factory.patch('/notes/',{'title':'Mogli'})

#     def test_patch(self):
#         factory = APIRequestFactory()
# #        request = factory.put('/notes/',{'title':'Mogli','content':'Jungle Jungle Baat Chali hai'})
#         request = factory.patch('/notes/',{'title':'Mogli'})
    
    # def test_encode(self):
    #     factory = RequestFactory()
    #     data = {'title':'Mogli','content':'Jungle Jungle Baat Chali hai'}
    #     content = encode_multipart('BoUnDaRyStRiNg',data)
    #     content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
    #     request =factory.put('/notes/547/', content, content_type=content_type)
    # def setUp(self):
    #     # Create a user with the desired username
    # #     self.user = User.objects.create_user(username='testuser', password='testpassword')
    # def setUp(self):
    #     # Create a user for testing
    #     self.user = User.objects.create_user(username='Ashish', password='password123')

    # def test_force_auth(self):
    #     factory = APIRequestFactory()
    #     user = User.objects.get(username ="Ashish")
    #     view = NoteListCreate.as_view()

    #     # Make an authenticated request to the view...
    #     request = factory.get(reverse('note-list-create'))
    #     force_authenticate(request, user=user)
    #     response = view(request)
    #     print(response)

    #     # Perform assertions on the response here
    #     self.assertEqual(response.status_code, 200)

    # def test_login(self):
    #     client =Client()
    #     client.login(username="Ashish",password="maa1997@")

    # def test_loout(self):
    #     client = Client()
    #     client.logout()
     
    #  def setUp(self):
    #     # Create a user for the test
    #     self.user = User.objects.create_user(username='Ashish', password='password123')

    #     # Create a token for the user
    #     self.token = Token.objects.create(user=self.user)
    #  def test_auth(self):
    #       token = Token.objects.get(user__username="Ashish")
    #       client = APIClient(enforce_csrf_checks=True)
    #       client.credentials(HTTP_AUTHORIZATION = 'Token' + token.key)
    #       client.credentials()
    #   def setUp(self):
    # #     # Create a user for the test
    #        self.user = User.objects.create_user(username='Ashish', password='password123')
    #        self.token = Token.objects.create(user=self.user)




    #   def test_request_client(self):
    #         client = RequestsClient()
    #         # Assuming you want to create a new note
    #         response = client.post('http://api/notes/', data={'title': 'New Note', 'content': 'Some content'})
    #         assert response.status_code,status.HTTP_201_CREATED



    #   def test_resquestclient(self):
    #         client = RequestsClient()
    #         response = client.get('http://api/notes/')
    #         assert response.status_code,status.HTTP_200_OK

#**************error********************

    #   def test_auth_basic(self):
    #         client = Client()
    #         client.auth = HTTPBasicAuth('user', 'pass')
    #         client.headers.update({'x-test': 'true'})

    #   def test_auth_basic(self):
    #     client = Client()
    #     # Set HTTP basic authentication credentials
    #     client.defaults['HTTP_AUTHORIZATION'] = 'Basic ' + HTTPBasicAuth('user', 'pass').username_password()
    #     # Set additional headers using defaults
    #     client.defaults['HTTP_X_TEST'] = 'true'

    #     # Now perform your test using the client

    #************error End*****************
    # def test_csrf_validate(self):
    #     client = Client(enforce_csrf_checks=True)

    #     # Obtain a CSRF token.
    #     response = client.get('http://api/notes/')
    #     assert response.status_code,status.HTTP_200_OK
    #     csrftoken = response.cookies['csrftoken'].value

    #     # Interact with the API.
    #     response = client.post('http://api/notes/', json={
    #         'name': 'MegaCorp',
    #         'status': 'active'
    #     }, headers={'X-CSRFToken': csrftoken})
    # #     assert response.status_code,status.HTTP_201_CREATED

    #    def test_create_account(self):
    #           create_data={
    #                  'title':'Junglebook',
    #                  'content':'Jungle Jungle Baat chali hai',
    #           }
    #           url = reverse('note-list-create')
    #           response =self.client.post(url,data=create_data,format='json')
    #           self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    #           self.assertEqual(Note.objects.count(),1)
    #           self.assertEqual(Note.objects.get().title,'Junglebook')
    #           self.assertEqual(Note.objects.get().content,'Jungle Jungle Baat chali hai')
    #           created_data = response.json()
    #           print(created_data)
        # def test_url_case(self):
        #     urlpatterns = [
        #              path('notes/', NoteListCreate.as_view(), name='note-list-create'),
        #            # path('notesrud/<int:pk>/',NoteListRetrive.as_view(), name='note-list-retrive'),
        #                           ]

        #     url =reverse('note-list-create')
        #     response= self.client.get(url,formal='json')
        #     self.assertEqual(response.status_code,status.HTTP_200_OK)
        #     self.assertEqual(len(response.data),1)
        # def setUp(self):
        # # Ensure the test data is created before running the tests
        #     Note.objects.create(title='Test Note', content='Test Content')
            
        # def test_url_case(self):
        #     url = reverse('note-list-create')
        #     response = self.client.get(url, format='json')
        #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        #     self.assertEqual(len(response.data), 1)
    

    
    #*********************Model Based test *************************************
    def setUp(self):
        self.note = Note.objects.create(title='Maa kasam', content='Badla Lunga')
    


    def test_note_creation(self):
        response =Note.objects.create(title="Maa kasam",content="Badla Lunga")
        self.assertEqual(response.title,"Maa kasam")
        self.assertEqual(response.content,"Badla Lunga")
        self.assertTrue(isinstance(response,Note))
        self.assertTrue(response.__str__(),response.title)
        self.assertTrue(response.__str__(),response.content)
        print(response.title)
        print(response.content)


    def test_note_get(self):
        _response = Note.objects.get(id=self.note.id)
        self.assertEqual(_response.title,'Maa kasam')
        self.assertEqual(_response.content,'Badla Lunga')
        self.assertTrue(_response.__str__(),_response.title)
        self.assertTrue(_response.__str__(),_response.content)
        print(_response.title)
        print(_response.content)

    def test_note2_get(self):
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.title,"Maa kasam")
        self.assertEqual(note.content,'Badla Lunga')
        print(note.title)
        print(note.content)

    def test_note_update(self):
        self.note.title = 'Maa kasam'
        self.note.content = 'Badla Lunga'
        self.note.save()
        updated_note = Note.objects.get(id=self.note.id)
        self.assertEqual(updated_note.title, 'Maa kasam')
        self.assertEqual(updated_note.content, 'Badla Lunga')

    def test_note_deletion(self):
        note_id = self.note.id
        self.note.delete()
        with self.assertRaises(Note.DoesNotExist):
            Note.objects.get(id=note_id)

    # def test_str_method(self):
    #     self.assertEqual(str(self.note), 'Maa kasam')

    
          



























    
    #********************Chat Gpt Suggestions **************************
        
    # def test_create_note(self):
    #     """
    #     Ensure we can create a new note.
    #     """
    #     url = reverse('note-list-create')
    #     data = {'title': 'DabApps', 'content': 'content of the note'}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Note.objects.count(), 1)
    #     self.assertEqual(Note.objects.get().title, 'DabApps')
    
    # def test_get_notes(self):
    #     """
    #     Ensure we can retrieve notes.
    #     """
    #     user = User.objects.create_user(username='testuser', password='testpass')
    #     self.client.force_authenticate(user=user)
    #     Note.objects.create(title='note1', content='content1')
    #     Note.objects.create(title='note2', content='content2')
    #     url = reverse('note-list-create')
    #     response = self.client.get(url, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 2)

    # def test_create_note(self):
    #     factory = APIRequestFactory()
    #     request = factory.post('/notes/', {'title': 'new idea', 'content': 'note content'}, format='json')
    #     view = NoteListCreate.as_view()
    #     response = view(request)

    # #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_authenticated_get_notes(self):
    #     factory = APIRequestFactory()
    #     user = User.objects.create_user(username='testuser', password='testpass')
    #     request = factory.get('/notes/')
    #     force_authenticate(request, user=user)
    #     view = NoteListCreate.as_view()
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

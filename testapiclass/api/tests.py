from django.test import TestCase
# Create your tests here.
from rest_framework.test import APIRequestFactory
from .views import NoteListCreate
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Note
import json
from django.test.client import encode_multipart, RequestFactory
from .views import NoteListRetrive,NoteListCreate
from django.contrib.auth.models import User






#basc
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
    def setUp(self):
        # Create a user with the desired username
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_force_auth(self):
        factory = APIRequestFactory()
        view = NoteListRetrive.as_view()

        # Make an authenticated request to the view...
        request = factory.get(reverse('note-list-create'))
        force_authenticate(request, user=self.user)
        response = view(request)

        # Perform assertions on the response here
        self.assertEqual(response.status_code, 200)





    
#     def test_create_note(self):
#         data = {
#             'title':'Junglebook',
#             'content':'Jungle Jungle Baat Chali hai'
#         }
#         _response = self.client.post(reverse('note-list-create'),data=data,format='json')
#         create_data = _response.json()
#         self.assertEqual(_response.status_code,status.HTTP_201_CREATED)
#         print(create_data)

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

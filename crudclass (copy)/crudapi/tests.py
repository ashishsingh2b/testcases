# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
   #**************************POST TESTAPIVIEW******************************
class StudentTest(APITestCase):
    def test_student_create(self):
        data = {
            'name':"Ashish",
            'roll':1212,
            'city':'Gopalganj',
        }
        url  = reverse('studentapi')
        _response = self.client.post(url,data=data,format='json')
        self.assertEqual(_response.status_code,status.HTTP_201_CREATED)
        response_data=_response.json()
        print(response_data)
        self.assertIn('id',response_data)
        self.assertEqual(response_data['name'],data['name'])
        self.assertEqual(response_data['roll'],data['roll'])
        self.assertEqual(response_data['city'],data['city'])

# #**************************GET TESTAPIVIEW******************************

    def test_get_student_data(self):
        data = {
            'name':"Ashish",
            'roll':1212,
            'city':'Gopalganj',
        }
        url =reverse('studentapi')
        _response = self.client.get(url,data=data,format='json')
        get_data = _response.json()
        self.assertEqual(_response.status_code,status.HTTP_200_OK)
        print(get_data)

    def test_put_testcase(self):
      create_data = {
        'name':'Ashish',
        'roll':1245,
        'city':'Surat'
      }
      create_response=self.client.post(reverse('studentapi'),data=create_data, format='json')
      # 
      #print(created_id)
      self.assertEqual(create_response.status_code,status.HTTP_201_CREATED)
      created_id =create_response.json()['id']
      print(created_id)


      url = reverse('studentapippd', kwargs={'pk': created_id})

      update_data={
         'name':'Bittu SIngh',
         'roll': 1997,
         'city':"Gopalganj"
      }

      response =self.client.put(url,data=update_data,format='json')
      print(response.content)
      self.assertEqual(response.status_code,status.HTTP_200_OK)

      # Assuming 'url' is the URL for the PATCH request
      update_response = self.client.patch(url, data=update_data, format='json')
      updated_data = update_response.json()
      print(updated_data)
     # ****************METHOD NOT ALLOW*********************
      # update_response=self.client.get(url,format='json')
      # updated_data = update_response.json()
      # print(updated_data)


#   Step 7: Assert that the resource has been updated correctly
      # self.assertEqual(updated_data['name'], update_data['name'])
      # self.assertEqual(updated_data['roll'], update_data['roll'])
      # self.assertEqual(updated_data['city'], update_data['city'])
      
    def test_stundet_patch(self):
        create_data = {
            'name':'Ashsih',
            'roll':1245,
            'city':'Surat'
        }
        _response = self.client.post(reverse('studentapi'),data=create_data,format='json')
        create_data_response = _response.json()['id']
        print(create_data_response)
        self.assertEqual(_response.status_code,status.HTTP_201_CREATED)

        url =reverse('studentapippd',kwargs={'pk':create_data_response})

        patch_data = {
            'name':'Ram ji',
            'city':'Ayodhya'
        }

        response=self.client.patch(url,data=patch_data,format='json')
        print(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        update_response=self.client.get(url,format='json')
        updated_data=update_response.json()
        print(updated_data)
    def test_student_delete(self):
         create_data = {
            'name':'Ashish',
            'roll':124,
            'city' :'Surat'
        }
         _response=self.client.post(reverse('studentapi'),data=create_data,format='json')
         self.assertEqual(_response.status_code,status.HTTP_201_CREATED)
         created_id = _response.json()['id']
         #print(created_id)

         url =reverse('studentapippd', kwargs={'pk':created_id})

         response = self.client.delete(url)
         print(response.content)
         self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

         get_delete_response=self.client.get(url,format='json')
         print(get_delete_response)
         self.assertEqual(get_delete_response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)










        









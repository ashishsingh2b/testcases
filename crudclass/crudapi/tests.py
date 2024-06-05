# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class StdTest(APITestCase):

    # def test_create_student(self):
    #     _data = {
    #         'name': 'Post Method',
    #         'roll': 111,
    #         'city': 'Surat'
    #     }

    #     url = reverse('studentapi')
    #     _response = self.client.post(url, data=_data, format="json")
    #     self.assertEqual(_response.status_code, status.HTTP_201_CREATED)

    #     response_data = _response.json()
    #     print(response_data)  # Add this line to see the actual response data
    #     self.assertIn('id', response_data)
    #     self.assertEqual(response_data['name'], _data['name'])
    #     self.assertEqual(response_data['roll'], _data['roll'])
    #     self.assertEqual(response_data['city'], _data['city'])
    
    # def test_get_blog(self):
    #     url =reverse('studentapi')
    #     _response = self.client.get(url,format='json')
    #     _data = _response.json()
    #     self.assertEqual(_response.status_code,status.HTTP_200_OK)
    #     print(_data)

    # def test_put_blog(self):
    #     # Step 1: Create an initial student entity
    #     create_data = {
    #         'name': 'Initial Name',
    #         'roll': 123,
    #         'city': 'Initial City'
    #     }
    #     create_response = self.client.post(reverse('studentapi'), data=create_data, format="json")
    #     self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
    #     created_id = create_response.json()['id']
        
    #     # Step 2: Define the URL for the created entity
    #     url = reverse('studentapippd', kwargs={'pk': created_id})  # Assuming the name of the detail route is 'studentapi-detail'

    #     # Step 3: Define the data to update the created entity
    #     update_data = {
    #         'name': 'Updated Blog Title',
    #         'roll': 123,  # Assuming roll number remains the same
    #         'city': 'Updated City'
    #     }
        
    #     # Step 4: Send a PUT request to update the entity
    #     response = self.client.put(url, data=update_data, format='json')
        
    #     # Print response content for debugging
    #     print(response.content)
        
    #     # Step 5: Verify the response status code
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    #     # Step 6: Fetch the updated resource to verify the changes
    #     updated_response = self.client.get(url, format='json')
    #     updated_data = updated_response.json()
        
    #     # Print updated data for debugging
    #     print(updated_data)
        
        # Step 7: Assert that the resource has been updated correctly
        # self.assertEqual(updated_data['name'], update_data['name'])
        # self.assertEqual(updated_data['roll'], update_data['roll'])
        # self.assertEqual(updated_data['city'], update_data['city'])

    def test_patch_blog(self):
    # Step 1: Create an initial student entity
        create_data = {
            'name': 'Initial Name',
            'roll': 123,
            'city': 'Initial City'
        }
        create_response = self.client.post(reverse('studentapi'), data=create_data, format="json")
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        created_id = create_response.json()['id']
        
        # Step 2: Define the URL for the created entity
        url = reverse('studentapippd', kwargs={'pk': created_id})  # Assuming the name of the detail route is 'studentapi-detail'

        # Step 3: Define the data to patch the created entity
        patch_data = {
            'name': 'Patched Name',
            'city': 'Patched City'
        }
        
        # Step 4: Send a PATCH request to update the entity
        response = self.client.patch(url, data=patch_data, format='json')
        
        # Print response content for debugging
        print(response.content)
        
        # Step 5: Verify the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Step 6: Fetch the updated resource to verify the changes
        updated_response = self.client.get(url, format='json')
        updated_data = updated_response.json()
        
        # Print updated data for debugging
        print(updated_data)
        
        # Step 7: Assert that the resource has been patched correctly
        self.assertEqual(updated_data['name'], patch_data['name'])
        # Since roll is not being patched, it should remain the same
        self.assertEqual(updated_data['roll'], create_data['roll'])
        self.assertEqual(updated_data['city'], patch_data['city'])
    #def test_delete_blog(self):
    # # Step 1: Create an initial student entity
    #     create_data = {
    #         'name': 'Initial Name',
    #         'roll': 123,
    #         'city': 'Initial City'
    #     }
    #     create_response = self.client.post(reverse('studentapi'), data=create_data, format="json")
    #     self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
    #     created_id = create_response.json()['id']
        
    #     # Step 2: Define the URL for the created entity
    #     url = reverse('studentapippd', kwargs={'pk': created_id})  # Assuming the name of the detail route is 'studentapi-detail'

    #     # Step 3: Send a DELETE request to delete the entity
    #     response = self.client.delete(url)
        
    #     # Print response content for debugging
    #     print(response.content)
        
    #     # Step 4: Verify the response status code
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    #     # Step 5: Try to fetch the deleted resource
    #     get_deleted_response = self.client.get(url, format='json')
        
    #     # Print deleted response content for debugging
    #     print(get_deleted_response.content)
        
    #     # Step 6: Verify that the resource has been deleted
    #     self.assertEqual(get_deleted_response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)



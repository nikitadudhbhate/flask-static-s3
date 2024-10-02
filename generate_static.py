from app import app
import os

def generate_static_files(output_folder='static_site'):
    with app.test_client() as client:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        response = client.get('/')
        with open(f'{output_folder}/index.html', 'wb') as f:
            f.write(response.data)

if __name__ == '__main__':
    generate_static_files()

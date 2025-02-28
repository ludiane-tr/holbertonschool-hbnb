from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Users

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    def get_user_by_uuid(self, user_id):
        return self.user_repo.get_by_attribute('id', user_id)
    
    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        user = self.user_repo.get(user_id)
        if not user:
            return None

        for field in ('first_name', 'last_name', 'email', 'password'):
            if field in user_data:
                setattr(user, field, user_data[field])

        self.user_repo.update(user_id, user)
        return user
    
    # Users
    
    # Amenities

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity_by_id(self, amenity_id):
        return self.amenity_repo.get_by_attribute('id', amenity_id)
    
    def get_amenity_by_name(self, amenity_name):
        return self.amenity_repo.get_by_attribute('name', amenity_name)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None

        for key in ('name', 'description'):
            if key in amenity_data:
                setattr(amenity, key, amenity_data[key])

        self.amenity_repo.update(amenity_id, amenity_data)
        return amenity

    
    # Amenities
    
    # Places
    # Places
    
    # Reviews
    # Reviews
    

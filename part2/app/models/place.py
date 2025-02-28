#!/usr/bin/python3

from typing import List
from datetime import datetime
from app.models.base_model import BaseModel
from .user import User
from .amenity import Amenity  # Assuming Amenity exists

class Place(BaseModel):
    __slots__ = (
        '_title', '_description', '_price', '_latitude', '_longitude', '_owner',
        '_reviews', '_amenities', '_created_at', '_updated_at'
    )

    def __init__(self, title: str, description: str, price: float, latitude: float, longitude: float, owner: User):
        """Initialize a new Place instance."""
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self._reviews: List = []
        self._amenities: List[Amenity] = []
        self._created_at: datetime = datetime.utcnow()
        self._updated_at: datetime = self._created_at

    def _validate_str(self, value: str, field: str, max_length: int = None):
        """Validate that value is a non-empty string with an optional max length."""
        if not isinstance(value, str) or not value:
            raise TypeError(f'{field} must be a non-empty string')
        if max_length and len(value) > max_length:
            raise ValueError(f'{field} must be {max_length} characters or less')

    def _validate_float(self, value: float, field: str, min_val: float = None, max_val: float = None):
        """Validate that value is a float within an optional range."""
        if not isinstance(value, float):
            raise TypeError(f'{field} must be a float')
        if min_val is not None and value < min_val:
            raise ValueError(f'{field} must be at least {min_val}')
        if max_val is not None and value > max_val:
            raise ValueError(f'{field} must be at most {max_val}')

    def _validate_owner(self, owner: User):
        """Validate that the owner is an instance of User."""
        if not isinstance(owner, User):
            raise TypeError('owner must be an instance of User')

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        self._validate_str(value, 'title', max_length=100)
        self._title = value
        self._updated_at = datetime.utcnow()

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        self._validate_str(value, 'description')
        self._description = value
        self._updated_at = datetime.utcnow()

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        self._validate_float(value, 'price', min_val=0.0)
        self._price = value
        self._updated_at = datetime.utcnow()

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, value: float):
        self._validate_float(value, 'latitude', min_val=-90.0, max_val=90.0)
        self._latitude = value
        self._updated_at = datetime.utcnow()

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, value: float):
        self._validate_float(value, 'longitude', min_val=-180.0, max_val=180.0)
        self._longitude = value
        self._updated_at = datetime.utcnow()

    @property
    def owner(self) -> User:
        return self._owner

    @owner.setter
    def owner(self, owner: User):
        self._validate_owner(owner)
        self._owner = owner
        self._updated_at = datetime.utcnow()

    def add_review(self, review) -> None:
        """Add a review to the place."""
        self._reviews.append(review)
        self._updated_at = datetime.utcnow()
        self.save()

    def add_amenity(self, amenity: Amenity) -> None:
        """Add an amenity to the place."""
        self._amenities.append(amenity)
        self._updated_at = datetime.utcnow()
        self.save()

    def create_place(self) -> None:
        """Create a new place (logic to persist it in the database can be added)."""
        self._created_at = datetime.utcnow()
        self._updated_at = self._created_at
        self.save()

    def update_place(self, **kwargs) -> None:
        """Update place attributes dynamically."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self._updated_at = datetime.utcnow()
        self.save()

    def delete_place(self) -> None:
        """Delete the place (logic to remove it from the database can be added)."""
        # Placeholder for delete logic
        del self

    def list_amenities(self) -> List[Amenity]:
        """Return a list of amenities for the place."""
        return self._amenities

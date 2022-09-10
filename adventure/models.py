from django.db import models
import uuid


class Object(models.Model):
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False)
    name = models.CharField(
        max_length=100,
        null=False,
    )
    description = models.CharField(max_length=255, blank=False)
    closerInspection = models.CharField(
        max_length=255, default='There is nothing of further interest here')


class Room(Object):
    # A location with a exits to the north, south, east, west, up and down directions
    north = models.ForeignKey('self',
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            related_name='goNorth')
    south = models.ForeignKey('self',
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            related_name='goSouth')
    east = models.ForeignKey('self',
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            related_name='goEast')
    west = models.ForeignKey('self',
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            related_name='goWest')
    up = models.ForeignKey('self',
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            related_name='goUp')
    down = models.ForeignKey('self',
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            related_name='goDown')

    def __str__(self):
        return self.name


class Item(Object):
    location = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    heldBy = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    weight = models.IntegerField(default=0)
    SIZE_CHOICES = [
        ('sm', 'Small'),
        ('md', 'Medium'),
        ('lg', 'Large'),
        ('xl', 'Large'),
        ('en', 'Enormous'),
    ]
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='sm')

    def pickUp(self, person):
        self.heldBy = person
        self.save()

    def __str__(self):
        return self.name


class Person(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=False,
    )
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    location = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)

    def move(self, loc):
        self.location = loc
        self.save()

    def __str__(self):
        return self.name

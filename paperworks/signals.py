from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files import File
from .models import Papermail

from django.conf import settings

import magic
from wand.image import Image
from os import remove

# génère un aperçu du fichier qui va remplacer le champ thumbnail par défaut

media_root = getattr(settings, 'MEDIA_ROOT')

@receiver(post_save, sender=Papermail)
def generate_thumbnail(sender,instance, **kwargs):
    
    mime = magic.Magic(mime=True)
    type_fichier = mime.from_file(instance.paper_file.path)
    nom_thumbnail = media_root + instance.name_file + '_thumb.jpeg'
    if not instance.thumbnail.name:

        if type_fichier == 'image/png' or type_fichier == 'image/jpeg':

            with Image(filename=instance.paper_file.path) as img:
                with img.clone() as converted:
                    converted.format = 'jpeg'
                    converted.resize(300,400)
                    converted.save(filename= nom_thumbnail)
                    fich = File(open(nom_thumbnail,'rb'))
                    instance.thumbnail.save(name = instance.name_file + '_thumb.jpeg', content = fich)
                    remove(nom_thumbnail)
                    
        elif type_fichier == 'application/pdf':

            with Image(filename=instance.paper_file.path + '[0]') as img:
                with img.clone() as converted:
                    converted.format = 'jpeg'
                    converted.save(filename= nom_thumbnail)
                    fich = File(open(nom_thumbnail,'rb'))
                    instance.thumbnail.save(name = instance.name_file + '_thumb.jpeg', content = fich)
                    remove(nom_thumbnail)

        else:
            pass
    else:
        pass
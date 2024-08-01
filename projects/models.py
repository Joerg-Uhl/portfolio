from django.db import models



class Project(models.Model):
    title = models.CharField(max_length=100)
    main_description = models.TextField()
    image = models.FileField(upload_to="project_images/", blank=True)
    order = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title


class Project_Details(models.Model):
    sk = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    code = models.TextField(blank=True)
    image = models.FileField(upload_to="project_images/", blank=True)

    def __str__(self):
        return self.description

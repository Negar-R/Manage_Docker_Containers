from django.db import models


class App(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length=255)
    command = models.CharField(max_length=255, null=True, blank=True)
    envs = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class AppContainerHistory(models.Model):
    # TODO: set it to cascade
    app = models.ForeignKey(App, null=True, on_delete=models.CASCADE)
    # As App object can be updated and it is possible to change its props, so it is required to consider
    # a new field for each of its props in this model.
    container_short_id = models.CharField(max_length=12, unique=True)
    container_name = models.CharField(max_length=255)
    container_image = models.CharField(max_length=255)
    container_command = models.CharField(max_length=255, null=True, blank=True)
    container_envs = models.JSONField(default=dict)
    container_status = models.CharField(max_length=100)
    container_logs = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.container_name

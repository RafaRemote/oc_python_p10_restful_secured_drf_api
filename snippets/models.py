from django.db import models

ROLES = [('r1', 'r1'), ('r2', 'r2'), ('r3', 'r3')]
PERMS = [('ADMIN', 'admin'), ('CONTRIB', 'contrib')]
TYPES = [('TYPE_1', 'type_1'), ('TYPE_2', 'type_2'), ('TYPE_3', 'type_3')]
TAGS = [('BUG', 'bug'), ('IMPROVEMENT', 'improvement'), ('TASK', 'task')]
PRIORITIES = [('LOW', 'low'), ('AVERAGE', 'average'), ('HIGH', 'high')]
STATUSES = [('TO_DO', 'to_do'), ('IN_PROGRESS', 'in_progress'), ('DONE', 'done')]


class Contributor(models.Model):
    user_id = models.ForeignKey('auth.User', related_name='contributors', on_delete=models.CASCADE)
    project_id = models.ForeignKey('project', related_name='contributors', on_delete=models.CASCADE)
    permission = models.CharField(choices=PERMS, default='p1', max_length=100)
    role = models.CharField(choices=ROLES, default='r1', max_length=100)


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(choices=TYPES, default='t1', max_length=100)
    author_user_id = models.ForeignKey('auth.User', related_name='projects', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    tag = models.CharField(choices=TAGS, default='ta1', max_length=100)
    priority = models.CharField(choices=PRIORITIES, default='pr1', max_length=100)
    status = models.CharField(choices=STATUSES, default='s1', max_length=100)
    project_id = models.ForeignKey('project', related_name='issues', on_delete=models.CASCADE)
    assignee_user_id = models.ForeignKey('auth.User', related_name='issues', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=255)
    author_user_id = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    issue_id = models.ForeignKey('issue', related_name='comments', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

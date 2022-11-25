from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок группы:',
        help_text='Введите название группы.'
    )
    slug = models.CharField(
        unique=True,
        max_length=50,
        verbose_name='Имя в адресной строке:',
        help_text='Введите уникальный индентификатор.'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание:',
        help_text='Добавьте описание группы.'
    )

    def __str__(self):
        return self.title


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подпиcячник:',
    )
    following = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE,
        verbose_name='Медиагигант:'
    )

    class Meta:
        models.UniqueConstraint(
            fields=['user', 'following'],
            name='unique_follow')


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True
    )
    group = models.ForeignKey(
        Group,
        related_name='posts',
        verbose_name='Группа:',
        help_text='Выберите группу для публикации.',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

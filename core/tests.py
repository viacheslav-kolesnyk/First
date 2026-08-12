from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from core.models import Task, Tag


class FirstListTests(TestCase):

    def setUp(self):
        # Create standard classification tags
        self.tag_work = Tag.objects.create(name="Work")
        self.tag_urgent = Tag.objects.create(name="Urgent")

        # Base time anchor for structural date progression
        now = timezone.now()

        # 1. Oldest task, marked as completed
        self.task_completed_old = Task.objects.create(
            content="Old Completed Task",
            is_done=True
        )
        # Manually alter creation date to simulate chronological order
        Task.objects.filter(pk=self.task_completed_old.pk).update(created_at=now - timedelta(days=3))

        # 2. Newer task, marked as completed
        self.task_completed_new = Task.objects.create(
            content="New Completed Task",
            is_done=True
        )
        Task.objects.filter(pk=self.task_completed_new.pk).update(created_at=now - timedelta(days=2))

        # 3. Oldest active task (not done)
        self.task_active_old = Task.objects.create(
            content="Old Active Task",
            is_done=False
        )
        Task.objects.filter(pk=self.task_active_old.pk).update(created_at=now - timedelta(days=1))

        # 4. Newest active task (not done)
        self.task_active_new = Task.objects.create(
            content="Newest Active Task",
            is_done=False
        )
        # Leaves default auto_now_add value for current time stamp

    def test_task_sorting_order(self):
        """Verifies tasks are sorted: 'not done' first, then from newest to oldest."""
        response = self.client.get(reverse("core:index"))
        tasks = list(response.context["tasks"])

        # Correct expected chronological/status layout order:
        # Index 0: Newest Active Task
        # Index 1: Old Active Task
        # Index 2: New Completed Task
        # Index 3: Old Completed Task
        self.assertEqual(tasks[0].content, "Newest Active Task")
        self.assertEqual(tasks[1].content, "Old Active Task")
        self.assertEqual(tasks[2].content, "New Completed Task")
        self.assertEqual(tasks[3].content, "Old Completed Task")

    def test_toggle_task_status_view(self):
        """Verifies the toggle endpoint flips the execution state and redirects."""
        # Target an uncompleted active task record item
        target_task = self.task_active_new
        self.assertFalse(target_task.is_done)

        # Trigger execution toggle view URL endpoint routing paths
        url = reverse("core:task-toggle", kwargs={"pk": target_task.pk})
        response = self.client.get(url)

        # Verify appropriate template redirect handling
        self.assertRedirects(response, reverse("core:index"))

        # Pull refreshed record status directly out from persistence state
        target_task.refresh_from_db()
        self.assertTrue(target_task.is_done)

        # Trigger it a second time to ensure it toggles back to incomplete
        self.client.get(url)
        target_task.refresh_from_db()
        self.assertFalse(target_task.is_done)

    def test_task_list_page_contains_required_elements(self):
        """Confirms template base structural markup contents render successfully."""
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Todo List")
        self.assertContains(response, "Add New Task")

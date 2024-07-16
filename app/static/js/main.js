function allowDrop(event) {
  event.preventDefault();
}

function drag(event) {
  event.dataTransfer.setData("text", event.target.id);
}

function drop(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  var taskItem = document.getElementById(data);

  if (!taskItem) {
      return;
  }

  var newTaskElement = event.target.closest('.task');
  if (!newTaskElement) {
      return;
  }

  var newTaskId = newTaskElement.id.split('-')[1];
  var taskItemId = taskItem.id.split('-')[2];

  var taskItemContainer = newTaskElement.querySelector('ol.task-items');
  if (!taskItemContainer) {
      return;
  }

  taskItemContainer.appendChild(taskItem);

  fetch('/update_task_item', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({
          task_item_id: taskItemId,
          new_task_id: newTaskId
      })
  });
}

function getDragAfterElement(container, y) {
  const draggableElements = [
      ...container.querySelectorAll("li[id*=task-item-]:not(.dragging)"),
  ];

  return draggableElements.reduce(
      (closest, child) => {
          const box = child.getBoundingClientRect();
          const offset = y - box.top - box.height / 2;
          if (offset < 0 && offset > closest.offset) {
              return { offset: offset, element: child };
          } else {
              return closest;
          }
      },
      { offset: Number.NEGATIVE_INFINITY }
  ).element;
}

function addDragAndDropEvents(draggable) {
  draggable.addEventListener("dragstart", (event) => {
      draggable.classList.add("dragging");
      drag(event);
  });

  draggable.addEventListener("dragend", () => {
      draggable.classList.remove("dragging");
  });
}

function initializeDragAndDrop() {
  const containers = document.querySelectorAll("section[id*=task-]");
  const draggables = document.querySelectorAll("li[id*=task-item-]");

  draggables.forEach((draggable) => {
      addDragAndDropEvents(draggable);
  });

  containers.forEach((container) => {
      container.addEventListener("dragover", (e) => {
          e.preventDefault();
          const afterElement = getDragAfterElement(container, e.clientY);
          const draggable = document.querySelector(".dragging");
          if (afterElement == null) {
              container.querySelector('ol.task-items').appendChild(draggable);
          } else {
              container.querySelector('ol.task-items').insertBefore(draggable, afterElement);
          }
      });

      container.addEventListener("drop", drop);
  });
}


initializeDragAndDrop();


document.addEventListener('htmx:afterSwap', (event) => {
  if (event.detail.target.id === 'modal_content') {
      const modal = document.getElementById('add_task_modal');
      if (modal) {
          modal.showModal();
      }
  }

  initializeDragAndDrop();
});

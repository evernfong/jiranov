/**
 * Jiranov UI Component
 * Handles interactive behaviour for the main card component.
 */
(function () {
  "use strict";

  var statusBadge = document.getElementById("status-badge");
  var actionBtn = document.getElementById("action-btn");
  var toggleBtn = document.getElementById("toggle-btn");
  var notification = document.getElementById("notification");

  var isActive = true;
  var notificationTimer = null;

  function showNotification(message) {
    if (notificationTimer) {
      clearTimeout(notificationTimer);
    }
    notification.textContent = message;
    notification.hidden = false;
    notificationTimer = setTimeout(function () {
      notification.hidden = true;
    }, 3000);
  }

  function updateStatus(active) {
    isActive = active;
    if (active) {
      statusBadge.textContent = "Active";
      statusBadge.classList.remove("card__badge--inactive");
    } else {
      statusBadge.textContent = "Inactive";
      statusBadge.classList.add("card__badge--inactive");
    }
  }

  actionBtn.addEventListener("click", function () {
    showNotification("Action completed successfully.");
  });

  toggleBtn.addEventListener("click", function () {
    updateStatus(!isActive);
    showNotification(
      isActive ? "Component activated." : "Component deactivated."
    );
  });
})();

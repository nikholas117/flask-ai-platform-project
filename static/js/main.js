// Utility function to format timestamps
function formatTimestamp(timestamp) {
  return new Date(timestamp).toLocaleString();
}

// Utility function to handle API errors
function handleApiError(error) {
  console.error("API Error:", error);
  return {
    error: true,
    message: "An error occurred while processing your request.",
  };
}

// Utility function to show loading state
function showLoading(elementId) {
  const element = document.getElementById(elementId);
  if (element) {
    element.classList.add("loading");
  }
}

// Utility function to hide loading state
function hideLoading(elementId) {
  const element = document.getElementById(elementId);
  if (element) {
    element.classList.remove("loading");
  }
}

// Add loading styles
const style = document.createElement("style");
style.textContent = `
    .loading {
        opacity: 0.5;
        pointer-events: none;
    }
`;
document.head.appendChild(style);



const ToggleButton = ({ onToggle, isDarkMode }) => {
  return (
    <button
      className={`toggle-button ${isDarkMode ? 'dark' : 'light'}`}
      onClick={onToggle}
    >
      {isDarkMode ? 'Light Mode' : 'Dark Mode'}
    </button>
  );
};

export default ToggleButton;

// Popup.js
import React, { useEffect, useState } from 'react';

const Popup = ({ isVisible, onClose }) => {
  // Automatically close the popup after 5 seconds
  useEffect(() => {
    if (isVisible) {
      const timer = setTimeout(onClose, 5000);
      return () => clearTimeout(timer); // Cleanup the timer when the component unmounts
    }
  }, [isVisible, onClose]);

  return (
    isVisible && (
      <div className="popup-container">
        <p>Oil spill detected!</p>
        <button onClick={onClose}>Close</button>
      </div>
    )
  );
};

export default Popup;

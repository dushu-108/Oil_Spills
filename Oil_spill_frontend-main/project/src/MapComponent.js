import React, { useState } from 'react';
import { MapContainer, TileLayer } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import MarkerLayer from './MarkerLayer';
import SearchBar from './SearchBar';
import Popup from './Popup';
import Sidebar from './Sidebar';
import { FaAdjust } from 'react-icons/fa'; // Import an icon from react-icons

const MapComponent = () => {
  const [isPopupVisible, setPopupVisible] = useState(false);
  const [isMapVisible, setMapVisible] = useState(true);
  const [isDarkTheme, setDarkTheme] = useState(true); // State for the map theme

  // Function to trigger oil spill event
  const handleOilSpill = () => {
    setPopupVisible(true);
  };

  // Toggle map visibility
  const toggleMapVisibility = () => {
    setMapVisible(!isMapVisible);
  };

  // Toggle map theme
  const toggleMapTheme = () => {
    setDarkTheme(!isDarkTheme);
  };

  return (
    <div className='Main_div'>
      <div className="sidebar-handle" />
      <Sidebar />
      <SearchBar />

      {/* Toggle Theme Button */}
      <button onClick={toggleMapTheme} className="toggle-theme-btn">
        <FaAdjust /> {/* Adjust icon */}
      </button>

      {/* Conditionally render the MapContainer */}
      {isMapVisible && (
        <MapContainer 
          center={[20, 0]} 
          zoom={2} 
          style={{ height: "100vh", width: "100%" }}
          minZoom={2}
          maxZoom={10}
          maxBounds={[[-85, -180], [85, 180]]}
          maxBoundsViscosity={1.0}
          zoomControl={false}
        >
          <TileLayer
            url={isDarkTheme ? "https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png" : "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"}
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
          />
          <MarkerLayer onOilSpill={handleOilSpill} />
        </MapContainer>
      )}

      {/* Render the Popup, visible based on state */}
      <Popup isVisible={isPopupVisible} onClose={() => setPopupVisible(false)} />
    </div>
  );
};

export default MapComponent;

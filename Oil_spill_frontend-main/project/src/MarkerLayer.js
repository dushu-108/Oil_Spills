import React, { useState,useEffect } from 'react';
import { CircleMarker, Popup } from 'react-leaflet';




// Function to generate random dummy data
const generateDummyData = (count) => {
    const dummyData = [];
    for (let i = 0; i < count; i++) {
        dummyData.push({
            id: i + 1,
            latitude: Math.random() * 180 - 90, // Latitude between -90 and 90
            longitude: Math.random() * 360 - 180, // Longitude between -180 and 180
            name: `Vessel ${i + 1}`,
            speed: Math.random() * 30, // Speed between 0 and 30 knots
            course: Math.random() * 360, // Course between 0 and 360 degrees
        });
    }
    return dummyData;
};

// Generated dummy data for 1000 vessels
const dummyData = generateDummyData(1000);

// Function to determine color based on vessel speed
const getColorBySpeed = (speed) => {
    if (speed < 5) return 'blue';
    if (speed < 10) return 'green';
    if (speed < 15) return 'yellow';
    if (speed < 20) return 'orange';
    return 'red';
};

const MarkerLayer = ({ onOilSpill }) => {
    //Function to assign data 

    const [vessels, setVessels] = useState([]);

    // Function to get data from api
    useEffect(()=>{
        fetchData();
    },[]);
    const fetchData = async ()=>{
        const data = await fetch("http://127.0.0.1:8023/vessels/")
        const result = await data.json();
       const realData = await result.slice(0, 5000);
        console.log(realData);
        setVessels(realData);
      
        
    }
    // Example function to simulate an oil spill
    const handleMarkerClick = () => {
        // Trigger the oil spill event
        onOilSpill();
    };
    console.log(vessels[2]);

    return (
        <>
            {vessels?.map((vessel) => (
                <CircleMarker
                    key={vessel.id}
                    center={[vessel.latitude, vessel.longitude]}
                    radius={3} // Adjust the size of the circle
                    fillColor={getColorBySpeed(vessel.sog)}
                    color={getColorBySpeed(vessel.sog)} // Border color same as fill color
                    fillOpacity={0.8}
                    eventHandlers={{
                        click: handleMarkerClick, // Attach the handler to the marker click event
                    }}
                >
                    <Popup>
                        <strong>Name:</strong> {vessel.name}<br />
                        <strong>Speed:</strong> {vessel.sog?.toFixed(2)} knots<br />
                        <strong>Course:</strong> {vessel.cog?.toFixed(2)}°
                    </Popup>
                </CircleMarker>
            ))}
        </>
    );
};

export default MarkerLayer;

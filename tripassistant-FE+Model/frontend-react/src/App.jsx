// src/App.jsx
import React, { useState } from "react";
import TripForm from "./components/TripForm";
import LocationCard from "./components/LocationCard";

const App = () => {
  const [results, setResults] = useState([]);

  return (
    <div style={{ maxWidth: "600px", margin: "auto", padding: "2rem" }}>
      <h1>Trợ lý AI gợi ý chuyến đi</h1>
      <TripForm onResults={setResults} />

      {results.length > 0 && (
        <>
          <h2>Kết quả gợi ý:</h2>
          {results.map((loc, index) => (
            <LocationCard key={index} location={loc} />
          ))}
        </>
      )}
    </div>
  );
};

export default App;
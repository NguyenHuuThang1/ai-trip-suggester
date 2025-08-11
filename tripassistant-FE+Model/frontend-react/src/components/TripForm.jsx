// src/components/TripForm.jsx
import React, { useState } from "react";
import axios from "axios";

const TripForm = ({ onResults }) => {
  const [query, setQuery] = useState("");
  const [maxCost, setMaxCost] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://localhost:8080/api/request-trip", {
        query,
        max_cost: parseInt(maxCost),
      });

      onResults(response.data);
    } catch (error) {
      console.error("Lỗi khi gọi API:", error);
      alert("Gợi ý thất bại. Vui lòng thử lại.");
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{
        display: "flex",
        gap: "10px",
        padding: "20px",
        background: "#f8fafc",
        borderRadius: "12px",
        boxShadow: "0 4px 8px rgba(0,0,0,0.05)",
        flexWrap: "wrap",
        alignItems: "flex-start",
      }}
    >
      <div style={{ flex: 2, display: "flex", flexDirection: "column" }}>
        <input
          type="text"
          placeholder="Nhập sở thích, điểm đến..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          required
          style={{
            padding: "10px 14px",
            borderRadius: "8px",
            border: "1px solid #cbd5e1",
            outline: "none",
            fontSize: "14px",
            marginBottom: "4px",
          }}
        />
        <small style={{ color: "#64748b", fontSize: "12px" }}>
          💡 Vui lòng nhập kèm từ khóa: Núi, Hang động, Biển, Lịch sử, Thiên nhiên, Miệt vườn.
        </small>
      </div>

      <div style={{ flex: 1, display: "flex", flexDirection: "column" }}>
        <input
          type="number"
          placeholder="Chi phí tối đa"
          value={maxCost}
          onChange={(e) => setMaxCost(e.target.value)}
          required
          style={{
            padding: "10px 14px",
            borderRadius: "8px",
            border: "1px solid #cbd5e1",
            outline: "none",
            fontSize: "14px",
            marginBottom: "4px",
            MozAppearance: "textfield",
          }}
          onWheel={(e) => e.target.blur()} // chặn cuộn thay đổi số
        />
        <small style={{ color: "#64748b", fontSize: "12px" }}>💰 Đơn vị: VND</small>
      </div>

      <button
        type="submit"
        style={{
          background: "linear-gradient(to right, #4f46e5, #3b82f6)",
          color: "white",
          border: "none",
          borderRadius: "8px",
          padding: "10px 20px",
          cursor: "pointer",
          fontSize: "14px",
          transition: "0.3s",
          whiteSpace: "nowrap",
          height: "42px",
          alignSelf: "flex-end",
        }}
        onMouseOver={(e) => (e.target.style.opacity = 0.85)}
        onMouseOut={(e) => (e.target.style.opacity = 1)}
      >
        🚀 Gợi ý
      </button>
    </form>
  );
};

export default TripForm;

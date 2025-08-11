// src/components/LocationCard.jsx
import React from "react";

const LocationCard = ({ location }) => (
  <div
    style={{
      background: "#ffffff",
      borderRadius: "12px",
      padding: "16px",
      margin: "8px 0",
      boxShadow: "0 4px 8px rgba(0,0,0,0.05)",
      border: "1px solid #e2e8f0",
      transition: "transform 0.2s ease, box-shadow 0.2s ease",
    }}
    onMouseOver={(e) => {
      e.currentTarget.style.transform = "translateY(-3px)";
      e.currentTarget.style.boxShadow = "0 6px 12px rgba(0,0,0,0.08)";
    }}
    onMouseOut={(e) => {
      e.currentTarget.style.transform = "translateY(0)";
      e.currentTarget.style.boxShadow = "0 4px 8px rgba(0,0,0,0.05)";
    }}
  >
    <h3 style={{ fontSize: "18px", fontWeight: "600", color: "#1e3a8a", marginBottom: "8px" }}>
      {location.ten}
    </h3>
    <p style={{ fontSize: "14px", color: "#475569", margin: "4px 0" }}>
      <strong>Mô tả:</strong> {location.mo_ta}
    </p>
    <p style={{ fontSize: "14px", color: "#475569", margin: "4px 0" }}>
      <strong>Vùng:</strong> {location.vung}
    </p>
    <p style={{ fontSize: "14px", color: "#475569", margin: "4px 0" }}>
      <strong>Loại:</strong> {location.loai}
    </p>
    <p style={{ fontSize: "14px", color: "#047857", fontWeight: "600", marginTop: "6px" }}>
      Chi phí: {location.chi_phi.toLocaleString()} VND
    </p>
  </div>
);

export default LocationCard;

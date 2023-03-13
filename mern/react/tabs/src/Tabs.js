import React, { useState } from "react";

const Tabs = (props) => {
  const [content, setContent] = useState(props.tabs[0].content);
  return (
    <div class="container">
      {props.tabs.map((tab, i) => (
        <div class="tab" key={i}>
          <button onClick={() => setContent(props.tabs[i].content)}>
            <strong>{tab.label}</strong>
          </button>
        </div>
      ))}
      <div class="content">{content}</div>
    </div>
  );
};

export default Tabs;

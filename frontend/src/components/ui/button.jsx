import React from 'react';

export function Button({ children, ...props }) {
  return (
    <button
      {...props}
      className="bg-primary text-white py-2 px-4 rounded hover:bg-primary-foreground"
    >
      {children}
    </button>
  );
}

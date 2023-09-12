export const dev = window.location.origin.includes('localhost') || window.location.origin.includes('127.0.0.1')
export const baseURL = dev ? 'https://localhost:5000' : ''

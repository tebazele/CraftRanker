export const dev = window.location.origin.includes('localhost') || window.location.origin.includes('127.0.0.1')
export const baseURL = dev ? 'http://localhost:5000' : ''

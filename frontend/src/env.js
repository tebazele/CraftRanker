export const dev = window.location.origin.includes('localhost') || window.location.origin.includes('127.0.0.1')
export const baseURL = dev ? 'http://localhost:5000' : ''
export const stripeKey = "pk_live_51IHajsHCtKGyoq0Uux1qljkVoVIQYIGz4zYYiRiSeGyeZi5dL1ivcXHbtt8r5opozts22qJgTOJVJRZql2kKrMph000swtYsKJ"
export const stripeTestModeKey = "pk_test_51IHajsHCtKGyoq0Ubpwmnr05B9GIFGrKvq1wUKEcFl44F1L2lIeK4UZD7Ynt63N8iQHJ7My32MCejELR6HwcKEGV00Bz3UHwLu"

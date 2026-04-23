output "alb_dns_name" {
  value       = "http://${aws_lb.main.dns_name}"
  description = "URL pública del dashboard"
}

output "ecr_repository_url" {
  value = aws_ecr_repository.app.repository_url
}
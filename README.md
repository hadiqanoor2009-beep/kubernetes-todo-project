# ☸️ Kubernetes To-Do Application

A containerized Flask To-Do application deployed on Kubernetes with MySQL, persistent storage, Kubernetes networking, security controls, health checks, and automatic scaling.

This project demonstrates practical Kubernetes and DevOps concepts including Deployments, Services, Ingress, StatefulSets, PersistentVolumeClaims, ConfigMaps, Secrets, RBAC, NetworkPolicies, probes, resource management, HPA, Docker, and Git/GitHub.

---

## 📌 Project Overview

The goal of this project is to deploy a Flask web application and MySQL database on Kubernetes while applying production-style Kubernetes concepts.

The Flask application runs as multiple replicas and communicates with MySQL through a Kubernetes Service.

The project also includes:

- Containerization with Docker
- Kubernetes Deployments
- Kubernetes Services
- Ingress
- MySQL StatefulSet
- Persistent storage
- ConfigMaps
- Secrets
- ServiceAccounts
- RBAC
- NetworkPolicy
- Readiness and liveness probes
- CPU and memory requests/limits
- Horizontal Pod Autoscaler
- Metrics Server
- Self-healing testing
- Database persistence testing
- Git/GitHub security practices

---

# 🏗️ Architecture

```text
                         ┌───────────────┐
                         │     User      │
                         └───────┬───────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │    Ingress    │
                         │  todo.local   │
                         └───────┬───────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │ todo-service  │
                         │     :80       │
                         └───────┬───────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
                    ▼                         ▼
             ┌──────────────┐         ┌──────────────┐
             │ Flask Pod 1  │         │ Flask Pod 2  │
             │    :5000     │         │    :5000     │
             └──────┬───────┘         └──────┬───────┘
                    │                         │
                    └────────────┬────────────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │ mysql-service │
                         │     :3306     │
                         └───────┬───────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │    MySQL      │
                         │    mysql-0    │
                         └───────┬───────┘
                                 │
                                 ▼
                         ┌───────────────┐
                         │ Persistent    │
                         │   Storage     │
                         │     1 Gi      │
                         └───────────────┘


       ┌──────────────────────────────────────────┐
       │          Kubernetes Components           │
       │                                          │
       │ HPA → Flask Deployment                   │
       │ ConfigMap → Database configuration      │
       │ Secret → Database credentials           │
       │ RBAC → Application permissions           │
       │ NetworkPolicy → MySQL traffic control   │
       │ Probes → Application health             │
       └──────────────────────────────────────────┘

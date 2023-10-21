package main

import (
	"fmt"
	"math/rand"
	"strconv"
	"github.com/gofiber/fiber/v2"
)

var senhaCorreta string

func main() {
	app := fiber.New()

	app.Get("/", func(c *fiber.Ctx) error {
		c.Type("html", "utf-8") // a codificação UTF-8 é para consertar problemas de texto
		htmlContent := `
		<!DOCTYPE html>
		<html>
		<head>
			<meta charset="UTF-8"> 
			<title>Gerar Senha</title>
		</head>
		<body>
			<form action="/gerar_senha" method="post">
				<input type="submit" value="Obter Senha">
			</form>
			<p>Sua senha é: <span id="senha">%s</span></p>
			<form action="/confirmarSenha" method="post">
				<input type="text" name="senhaUsuario" placeholder="Digite sua senha">
				<input type="submit" value="Confirmar">
			</form>
		</body>
		</html>
		`
		return c.SendString(fmt.Sprintf(htmlContent, senhaCorreta))//senhaCorreta é adicionada ao %s
	})

	app.Post("/gerar_senha", func(c *fiber.Ctx) error {
		senhaAleatoria := rand.Intn(10) + 1
		senhaCorreta = strconv.Itoa(senhaAleatoria)
		return c.Redirect("/")
	})

	app.Post("/confirmarSenha", func(c *fiber.Ctx) error {
		senhaDigitada := c.FormValue("senhaUsuario")
		if senhaDigitada == senhaCorreta {
			return c.Redirect("/nova_pagina")
		} else {
			return c.SendString("Senha incorreta. Tente novamente!")
		}
	})

	app.Get("/nova_pagina", func(c *fiber.Ctx) error {
		c.Type("html", "utf-8") 
		htmlContent := `
		<!DOCTYPE html>
		<html>
		<head>
			<meta charset="UTF-8">
			<title>Nova Página</title>
		</head>
		<body>
			<h2>Sua carta é: %s</h2>
		</body>
		</html>
		`
		index, _ := strconv.Atoi(senhaCorreta)
		index--
		cartas := []string{"As de Copas", "2 de Copas", "8 de Espadas", "As de Ouro", "K de Paus", "6 de Espadas", "J de Copas", "3 de Ouro", "As de Paus", "J de Ouro"}
		carta := cartas[index]
		return c.SendString(fmt.Sprintf(htmlContent, carta))
	})

	app.Listen(":3000")
}

package credentials

import (
	"fmt"
	"os"

	"gopkg.in/ini.v1"
)

const credentialsPath string = "/.gha/config"

func (c *Credentials) Set() error {
	home := os.Getenv("HOME")
	_, err := os.Stat(home + credentialsPath)
	if err != nil {
		return err
	} else {
		cfg, err := ini.Load(home + credentialsPath)
		if err != nil {
			return fmt.Errorf("Failed to open file: %v", err)
		} else {
			if value, err := readFromSection(cfg, "credentials", "token"); err == nil {
				c.token = value
			} else {
				return fmt.Errorf("Failed to read file: %v", err)
			}
			if value, err := readFromSection(cfg, "credentials", "owner"); err == nil {
				c.Owner = value
			} else {
				return fmt.Errorf("Failed to read file: %v", err)
			}
			if value, err := readFromSection(cfg, "credentials", "repo"); err == nil {
				c.Repo = value
			} else {
				return fmt.Errorf("Failed to read file: %v", err)
			}
			fmt.Println("credentials set up")
			return nil
		}
	}
}

func readFromSection(cfg *ini.File, section string, key string) (string, error) {
	if key := cfg.Section(section).Key(key); key != nil {
		return key.String(), nil
	} else {
		return "", fmt.Errorf("no %s key in section %s", key, section)
	}
}

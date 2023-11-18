#gpt3 #dreambot 

``` Java

import org.dreambot.api.methods.Calculations;
import org.dreambot.api.methods.container.impl.equipment.EquipmentSlot;
import org.dreambot.api.methods.map.Area;
import org.dreambot.api.methods.skills.Skill;
import org.dreambot.api.methods.tabs.Tab;
import org.dreambot.api.script.AbstractScript;
import org.dreambot.api.script.Category;
import org.dreambot.api.script.ScriptManifest;

@ScriptManifest(author = "YourNameHere", name = "Zulrah Bot", version = 1.0, description = "Kills Zulrah for profits", category = Category.COMBAT)
public class ZulrahBot extends AbstractScript {

    private Area zulrahArea;

    private int zulrahHP;
    private int zulrahMinHP;

    private boolean inCombat;

    @Override
    public void onStart() {
        zulrahArea = new Area(2268, 3073, 2287, 3105);
        zulrahHP = 100;
        zulrahMinHP = 0;
        inCombat = false;
    }

    @Override
    public int onLoop() {
        // If we're not in the zulrah area, teleport there
        if (!zulrahArea.contains(getLocalPlayer())) {
            getTabs().open(Tab.MAGIC);
            getMagic().castSpell("Teleport to Zul-Andra");
            return Calculations.random(500, 1500);
        }

        // Check if in combat
        if (getLocalPlayer().isInCombat()) {
            inCombat = true;
        } else if (inCombat) {
            // Check if Zulrah is dead
            if (getLocalPlayer().getHealthPercent() == 100) {
                inCombat = false;
                getWalking().walk(zulrahArea.getRandomTile());
                return Calculations.random(1000, 2000);
            }
        }

        // Check if we have the correct equipment for Zulrah
        if (!getEquipment().isWearingItem(EquipmentSlot.HAT, "Crown")) {
            // Equip the crown
            getInventory().interact("Crown", "Wear");
            return Calculations.random(1000, 1500);
        }

        // Check if we are at the right level
        if (getSkills().getRealLevel(Skill.SLAYER) < 75) {
            // Stop the script
            stop();
            return 0;
        }

        // Check if we need to attack Zulrah
        if (!inCombat) {
            // Attack Zulrah
            getNpcs().closest("Zulrah").interact("Attack");
            return Calculations.random(1000, 2000);
        }

        // Check if we need to heal
        if (getLocalPlayer().getHealthPercent() < zulrahMinHP) {
            // Eat food
            getInventory().interact("Lobster", "Eat");
            return Calculations.random(1000, 1500);
        }

        // Check if we need to drink a potion
        if (getLocalPlayer().getHealthPercent() < zulrahHP) {
            // Drink a potion
            getInventory().interact("Super restore(4)", "Drink");
            return Calculations.random(1000, 1500);
        }

        return Calculations.random(500, 1000);
    }

}
```

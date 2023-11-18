#codex #dreambot 

Below is an example of a Hill Giants bot using the Dreambot API and Java that can be used to farm Hill Giants. 

``` Java
Below is an example of a Hill Giants bot using the Dreambot API and Java that can be used to farm Hill Giants.

import org.dreambot.api.script.Category;
import org.dreambot.api.script.ScriptManifest;
import org.dreambot.api.methods.Game;
import org.dreambot.api.methods.filter.Filter;
import org.dreambot.api.methods.map.Area;
import org.dreambot.api.methods.map.Tile;
import org.dreambot.api.methods.walking.path.Path;
import org.dreambot.api.script.AbstractScript;
import org.dreambot.api.wrappers.interactive.NPC;
import org.dreambot.api.methods.container.impl.EquipmentSlot;

@ScriptManifest(description = "Kills Hill Giants", category = Category.COMBAT, name = "Hill Giants Bot")
public class HillGiantsBot extends AbstractScript {

    private Area hillGiantsArea = new Area(3080, 9864, 3109, 9834);
    private Filter<NPC> giants = n -> n != null && n.getName().equals("Hill Giant") && n.hasAction("Attack");

    @Override
    public void onStart() {

        if (Game.getClientState() == Game.INDEX_MAP_LOADED) {
            log("Starting HillGiantsBot...");

            getWalking().webWalk(hillGiantsArea);
            sleepUntil(() -> hillGiantsArea.contains(getLocalPlayer()), 10000);
            log("Arrived at Hill Giants area.");
        }
    }

    @Override
    public int onLoop() {

        if (getEquipment().isWeaponEquipped(EquipmentSlot.MAIN_HAND)) {

            NPC target = getNpcs().closest(giants);
            if (target != null) {
                if (target.isOnScreen()) {
                    target.interact("Attack");
                    log("Fighting Hill Giant");
                    sleep(2500, 6000);
                } else {
                    getWalking().walk(target);
                    sleepUntil(() -> target.isOnScreen(), 6000);
                }
            } else {
                Path p = getWalking().generatePath(target.getLocation());
                if (p != null) {
                    p.step();
                    sleepUntil(() -> getLocalPlayer().isMoving(), 9000);
                }
            }

        } else {
            getInventory().interact("Steel axe", "Wield");
            sleep(1500, 4000);
        }
        return 0;
    }

}
```
